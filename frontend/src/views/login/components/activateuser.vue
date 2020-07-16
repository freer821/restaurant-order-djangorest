<template>
  <div>
    <el-form ref="activecodeForm" :model="activecodeForm" :rules="rules" label-width="80px">
      <el-form-item label="激活码" prop="activecode">
        <el-input v-model="activecodeForm.activecode" placeholder="请输入用户名" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit('activecodeForm')">激活</el-button>
      </el-form-item>

    </el-form>
  </div>
</template>

<script>
import { activateUser } from '@/api/login'

export default {
  name: 'Activateuser',
  data() {
    return {
      activecodeForm: {
        activecode: ''
      },
      rules: {
        activecode: [
          { required: true, message: '激活码', trigger: 'blur' }
        ]
      }

    }
  },
  methods: {
    onSubmit(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          activateUser(this.activecodeForm).then(resonpse => {
            this.$message.success(resonpse.msg)
            this.$refs[formName].resetFields()
            this.$emit('eventCloseDialog', 'close')
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
