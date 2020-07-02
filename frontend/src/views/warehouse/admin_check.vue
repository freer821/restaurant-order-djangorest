<template>
  <div class="app-container">

    <el-card class="box-card">
      <h3>检修</h3>
      <el-radio-group v-model="check_type" style="padding: 20px">
        <el-radio-button label="massiv"> 批量录入</el-radio-button>
        <el-radio-button label="single"> 详细录入</el-radio-button>
      </el-radio-group>
      <el-form v-if="check_type==='massiv'" ref="ware_massiv_check" :rules="rules" :model="ware_massiv_check" label-width="150px">
        <el-form-item label="产品名称" prop="product_name">
          <el-input v-model="ware_massiv_check.product_name" />
        </el-form-item>
        <el-form-item
          label="状态"
        >
          <el-select v-model="ware_massiv_check.status" clearable placeholder="请选择">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item
          label="数量"
          prop="num"
        >
          <el-input v-model="ware_massiv_check.num" type="number" placeholder="0" />
        </el-form-item>
      </el-form>
      <el-form v-else ref="ware_single_check" :rules="rules" :model="ware_single_check" label-width="150px">
        <el-form-item label="产品名称" prop="product_name">
          <el-input v-model="ware_single_check.product_name" />
        </el-form-item>
        <el-form-item
          label="状态"
        >
          <el-select v-model="ware_single_check.status" clearable placeholder="请选择">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item v-if="ware_single_check.status==='error1'" label="故障类型" prop="error_status">
          <el-checkbox-group v-model="ware_single_check.error_status">
            <el-checkbox label="hardware">硬件</el-checkbox>
            <el-checkbox label="software">软件</el-checkbox>
          </el-checkbox-group>
        </el-form-item>
        <el-form-item
          label="数量"
          prop="num"
        >
          <el-input v-model="ware_single_check.num" type="number" placeholder="0" disabled />
        </el-form-item>
        <el-form-item
          label="SN Code"
          prop="sn_code"
        >
          <el-input v-model="ware_single_check.sn_code" />
        </el-form-item>
        <el-form-item
          label="备注"
          prop="descrp"
        >
          <el-input v-model="ware_single_check.descrp" type="textarea" :rows="2" />
        </el-form-item>
      </el-form>
    </el-card>
    <div class="op-container">
      <el-button @click="resetForm">重置</el-button>
      <el-button type="primary" @click="submitForm">录入</el-button>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'WarehouseCheck',

  data() {
    return {
      ware_massiv_check: {
        logistic_code: '',
        product_name: '',
        num: 0,
        status: 'normal'
      },
      ware_single_check: {
        logistic_code: '',
        product_name: '',
        num: 1,
        status: 'normal',
        sn_code: '',
        descrp: '',
        error_status: []
      },
      rules: {
        product_name: [{ required: true, message: '产品名称不能为空', trigger: 'blur' }]
      },
      check_type: 'massiv',
      options: [{
        value: 'normal',
        label: '良品'
      }, {
        value: 'error0',
        label: '废品 - 划痕'
      }, {
        value: 'error1',
        label: '废品 - 故障'
      }]
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
      this.ware_massiv_check = {
        logistic_code: '',
        product_name: '',
        num: 0,
        status: 'normal'
      }
      this.ware_single_check = {
        logistic_code: '',
        product_name: '',
        num: 1,
        status: 'normal',
        sn_code: '',
        descrp: '',
        error_status: []
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
