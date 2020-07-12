<template>
  <div class="app-container">
    <el-form ref="prfileForm" :rules="rules" :model="profile" status-icon label-position="left" label-width="100px" style="width: 400px; margin-left:50px;">
      <el-form-item label="用户名">
        <el-input v-model="username" disabled />
      </el-form-item>

      <el-form-item label="公司名称" prop="company_name">
        <el-input v-model="profile.company_name" />
      </el-form-item>
      <el-form-item label="公司地址" prop="company_addr">
        <el-input v-model="profile.company_addr" />
      </el-form-item>
      <el-form-item label="公司电话" prop="company_tel">
        <el-input v-model="profile.company_tel" />
      </el-form-item>
    </el-form>
    <div style="margin-left:100px;">
      <el-button type="primary" @click="change">修改</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Notice',
  data() {
    return {
      username: this.$store.getters.username,
      profile: {
        company_name: this.$store.getters.profile.company_name,
        company_addr: this.$store.getters.profile.company_addr,
        company_tel: this.$store.getters.profile.company_tel
      },
      rules: {
        company_name: [
          { required: true, message: '不能为空', trigger: 'blur' }
        ]
      }

    }
  },
  methods: {
    change() {
      this.$refs['prfileForm'].validate((valid) => {
        if (!valid) {
          return
        }
        this.$store.dispatch('updateProfile', { 'profile': this.profile }).then(() => {
          this.$notify.success({
            title: '成功',
            message: '个人信息修改成功'
          })
        })
      })
    }

  }
}
</script>
