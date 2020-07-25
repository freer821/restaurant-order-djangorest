<template>
  <div>
    <el-form ref="passwordForgottenForm" :model="passwordForgottenForm" :rules="rules" label-width="80px">
      <el-form-item label="用户名" prop="username">
        <el-input v-model="passwordForgottenForm.username" placeholder="请输入用户名" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit('passwordForgottenForm')">密码重置</el-button>
      </el-form-item>

    </el-form>
  </div>
</template>

<script>
import { resetpassword } from '@/api/login'

export default {
  name: 'PasswordForgotten',
  data() {
    return {
      passwordForgottenForm: {
        username: ''
      },
      rules: {
        username: [
          { required: true, message: '用户名不允许为空', trigger: 'blur' },
          { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
        ]
      }

    }
  },
  methods: {
    onSubmit(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          resetpassword(this.passwordForgottenForm).then(resonpse => {
            this.$message.success(resonpse.msg)
            this.$refs[formName].resetFields()
            this.$emit('eventCloseDialog', 'reset')
          }).catch(err => {
            this.$message.error(err.msg)
          })
        } else {
          return false
        }
      })
    }
  }

}
</script>
