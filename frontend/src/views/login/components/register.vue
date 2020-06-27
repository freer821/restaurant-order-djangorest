<template>
  <div>
    <el-form ref="ruleForm" :model="ruleForm" status-icon :rules="rules" label-width="100px">
      <el-form-item label="用户名" prop="username">
        <el-input v-model="ruleForm.username" type="email" autocomplete="off" />
      </el-form-item>
      <el-form-item label="密码" prop="pass">
        <el-input v-model="ruleForm.pass" type="password" autocomplete="off" />
      </el-form-item>
      <el-form-item label="确认密码" prop="checkPass">
        <el-input v-model="ruleForm.checkPass" type="password" autocomplete="off" />
      </el-form-item>
      <el-form-item label="公司名称" prop="company">
        <el-input v-model.number="ruleForm.company" />
      </el-form-item>
      <el-form-item label="公司地址" prop="company_addr">
        <el-input v-model.number="ruleForm.company_addr" />
      </el-form-item>
      <el-form-item label="公司电话" prop="company_tel">
        <el-input v-model.number="ruleForm.company_tel" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
        <el-button @click="resetForm('ruleForm')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { register } from '@/api/login'
export default {
  data() {
    const validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.ruleForm.checkPass !== '') {
          this.$refs.ruleForm.validateField('checkPass')
        }
        callback()
      }
    }
    const validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.ruleForm.pass) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      ruleForm: {
        username: '',
        pass: '',
        checkPass: '',
        company: '',
        company_addr: '',
        company_tel: ''

      },
      rules: {
        username: [
          { required: true, message: '用户名不允许为空', trigger: 'blur' },
          { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
        ],
        pass: [
          { required: true, message: '密码不允许为空', trigger: 'blur' },
          { validator: validatePass, trigger: 'blur' }
        ],
        checkPass: [
          { required: true, message: '确认密码不允许为空', trigger: 'blur' },
          { validator: validatePass2, trigger: 'blur' }
        ],
        company: [
          { required: true, message: '公司名称不允许为空', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          const register_data = {
            username: this.ruleForm.username,
            password: this.ruleForm.pass,
            profile: {
              company_name: this.ruleForm.company,
              company_addr: this.ruleForm.company_addr,
              company_tel: this.ruleForm.company_tel
            }
          }
          register(register_data).then(response => {
            this.$message.success('注册成功，请前往您的邮箱激活账号！')
            this.$refs[formName].resetFields()
            this.$emit('eventCloseDialog', 'register')
          }).catch(err => {
            this.$message.error(JSON.stringify(err.msg))
          })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm(formName) {
      this.$refs[formName].resetFields()
    }
  }
}
</script>
