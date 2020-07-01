<template>
  <div class="app-container">

    <el-card class="box-card">
      <h3>检修</h3>
      <el-form ref="ware_check" :rules="rules" :model="ware_check" label-width="150px">
        <el-form-item label="产品名称" prop="product_name">
          <el-input v-model="ware_check.product_name" />
        </el-form-item>
        <el-form-item
          label="数量"
          prop="real_num"
        >
          <el-input v-model="ware_check.real_num" type="number" placeholder="0" />
        </el-form-item>
        <el-form-item label="SN码">
          <el-input v-model="ware_check.admin_extra.sn_codes" type="textarea" :rows="2" placeholder="多个SN码，中间以英文逗号(,)隔开" />
        </el-form-item>
      </el-form>
    </el-card>
    <div class="op-container">
      <el-button @click="resetForm">重置</el-button>
      <el-button type="primary" @click="submitForm">入库</el-button>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'RukuHandle',

  data() {
    return {
      ware_check: {
        logistic_code: '',
        product_name: '',
        admin_extra: {
          sn_codes: ''
        }
      },
      rules: {
        product_name: [{ required: true, message: '产品名称不能为空', trigger: 'blur' }],
        real_num: [
          { required: true, message: '不能为空或非数字', trigger: 'blur' }
        ],
        logistic_code: [{ required: true, message: '快递单号不能为空', trigger: 'blur' }]
      }
    }
  },
  computed: {
    ...mapGetters([
      'current_user'
    ])
  },
  methods: {
    submitForm() {
      this.$refs.ware_check.validate((valid) => {
        if (valid && this.current_user !== 'all') {
        } else {
          this.$message.error('请检查输入，并查看当前操作用户是否正确！')
          return false
        }
      })
    },
    resetForm() {
      this.ware_check = {
        product_name: '',
        admin_extra: {
          sn_codes: ''
        }
      }
    }
  }
}
</script>

<style scoped>
  .el-card {
    margin-bottom: 10px;
  }
  .el-form {
    width: 50% !important;
  }
</style>
