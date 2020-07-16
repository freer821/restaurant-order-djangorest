<template>
  <div class="login-container">
    <el-form
      ref="loginForm"
      :model="loginForm"
      :rules="loginRules"
      class="login-form"
      auto-complete="on"
      label-position="left"
    >
      <div class="title-container">
        <h3 class="title">Warehouse System</h3>
      </div>
      <el-form-item prop="username">
        <span class="svg-container">
          <svg-icon icon-class="user" />
        </span>
        <el-input
          v-model="loginForm.username"
          name="username"
          type="text"
          tabindex="1"
          auto-complete="on"
          placeholder="账户"
        />
      </el-form-item>

      <el-form-item prop="password">
        <span class="svg-container">
          <svg-icon icon-class="password" />
        </span>
        <el-input
          v-model="loginForm.password"
          :type="passwordType"
          name="password"
          auto-complete="on"
          tabindex="2"
          show-password
          placeholder="密码"
          @keyup.enter.native="handleLogin"
        />
      </el-form-item>

      <el-button
        :loading="loading"
        type="primary"
        style="width:100%;margin-bottom:50px;"
        @click.native.prevent="handleLogin"
      >登录</el-button>

      <div style="position:relative">
        <div class="tips">
          <span>
            <el-link type="warning" @click="passwordForgottenDialog=true">忘记密码</el-link>
          </span>
          <span>
            <el-link type="danger" @click="activateUserDialog=true">激活账户</el-link>
          </span>
        </div>
        <el-button class="thirdparty-button" type="danger" @click="rigisterDialog=true">会员注册</el-button>
      </div>
    </el-form>
    <el-dialog title="忘记密码?" :visible.sync="passwordForgottenDialog">
      <password-forgotten @eventCloseDialog="closeDialog" />
    </el-dialog>
    <el-dialog title="账户激活" :visible.sync="activateUserDialog">
      <activateuser @eventCloseDialog="closeDialog" />
    </el-dialog>
    <el-dialog title="会员注册" :visible.sync="rigisterDialog">
      <register @eventCloseDialog="closeDialog" />
    </el-dialog>

  </div>
</template>

<script>
import PasswordForgotten from './components/passwordforgotten'
import Register from './components/register'
import Activateuser from '@/views/login/components/activateuser'

export default {
  name: 'Login',
  components: { PasswordForgotten, Register, Activateuser },
  data() {
    const validatePassword = (rule, value, callback) => {
      if (value.length < 3) {
        callback(new Error('管理员密码长度应大于3'))
      } else {
        callback()
      }
    }
    return {
      loginForm: {
        username: '',
        password: ''
      },
      loginRules: {
        username: [
          { required: true, message: '用户名不允许为空', trigger: 'blur' },
          { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
        ],
        password: [
          { required: true, message: '密码不允许为空', trigger: 'blur' },
          { validator: validatePassword, trigger: 'blur' }
        ]
      },
      passwordType: 'password',
      loading: false,
      passwordForgottenDialog: false,
      activateUserDialog: false,
      rigisterDialog: false,
      form: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      }
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        this.redirect = route.query && route.query.redirect
      },
      immediate: true
    }
  },
  methods: {
    handleLogin() {
      this.$refs.loginForm.validate(valid => {
        if (valid && !this.loading) {
          this.loading = true
          this.$store
            .dispatch('LoginByUsername', this.loginForm)
            .then(() => {
              this.loading = false
              this.$router.push({ path: this.redirect || '/' })
            })
            .catch(response => {
              this.$notify.error({
                title: '失败',
                message: response.msg
              })
              this.loading = false
            })
        } else {
          return false
        }
      })
    },
    closeDialog(dialogname) {
      if (dialogname === 'register') {
        this.rigisterDialog = false
      }
      if (dialogname === 'reset') {
        this.passwordForgottenDialog = false
      }
    }
  }
}
</script>

<style lang="scss">
/* 修复input 背景不协调 和光标变色 */
/* Detail see https://github.com/PanJiaChen/vue-element-admin/pull/927 */

$bg: #283443;
$light_gray: #fff;
$cursor: #fff;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .login-container .login-form .el-input input {
    color: $cursor;
  }
}

/* reset element-ui css */
.login-container .login-form {
  .el-input {
    display: inline-block;
    width: 85%;
    height: 47px;

    input {
      height: 47px;
      padding: 12px 5px 12px 15px;
      color: $light_gray;
      background: transparent;
      border: 0;
      border-radius: 0;

      -webkit-appearance: none;
      caret-color: $cursor;

      &:-webkit-autofill {
        box-shadow: 0 0 0 1000px $bg inset !important;

        -webkit-text-fill-color: $cursor !important;
      }
    }
  }

  .el-form-item {
    color: #454545;
    background: rgba(0, 0, 0, .1);
    border: 1px solid rgba(255, 255, 255, .1);
    border-radius: 5px;
  }
}
</style>

<style lang="scss" scoped>
$bg: #2d3a4b;
$dark_gray: #889aa4;
$light_gray: #eee;

.login-container {
  min-height: 100%;
  width: 100%;
  background-color: $bg;
  overflow: hidden;

  .login-form {
    position: relative;
    width: 520px;
    max-width: 100%;
    padding: 160px 35px 0;
    margin: 0 auto;
    overflow: hidden;
  }

  .tips {
    font-size: 14px;
    color: #fff;
    margin-bottom: 10px;

    span {
      &:first-of-type {
        margin-right: 16px;
      }
    }
  }

  .svg-container {
    padding: 6px 5px 6px 15px;
    color: $dark_gray;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }

  .thirdparty-button {
    position: absolute;
    right: 0;
    bottom: 6px;
  }

  .title-container {
    position: relative;

    .title {
      font-size: 26px;
      color: $light_gray;
      margin: 0px auto 40px auto;
      text-align: center;
      font-weight: bold;
    }
  }
}
</style>

