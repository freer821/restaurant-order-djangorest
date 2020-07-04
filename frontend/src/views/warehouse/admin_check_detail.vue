<template>
  <div class="app-container">

    <el-card class="box-card">
      <h3>检修 - 详细录入</h3>
      <el-form ref="ware_single_check" :model="ware_single_check" label-width="150px">
        <el-form-item label="产品名称" prop="product_name">
          <el-input v-model="ware_single_check.product_name" disabled />
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
          <el-checkbox-group v-model="ware_single_check.descrp.error_status">
            <el-checkbox label="hardware">硬件</el-checkbox>
            <el-checkbox label="software">软件</el-checkbox>
          </el-checkbox-group>
        </el-form-item>
        <el-form-item
          label="数量"
          prop="num"
        >
          <el-input value="1" type="number" disabled />
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
          <el-input v-model="ware_single_check.descrp.comment" type="textarea" :rows="2" />
        </el-form-item>
      </el-form>
    </el-card>
    <div class="op-container">
      <el-button @click="resetForm">重置</el-button>
      <el-button type="primary" @click="submitForm">更新</el-button>
    </div>
  </div>
</template>

<script>
import { getDetailCheckedWare, editDetailCheckedWare } from '@/api/warehouse'
import { mapGetters } from 'vuex'
export default {
  name: 'WarehouseCheckDetail',

  data() {
    return {
      ware_single_check: {
        product_name: '',
        status: 'normal',
        sn_code: '',
        descrp: {
          comment: '',
          error_status: []
        }
      },
      origin_ware_single_check: {},
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
  created() {
    getDetailCheckedWare(this.$route.query.id).then(respone => {
      this.origin_ware_single_check = respone.data
      this.ware_single_check = this.origin_ware_single_check
    }).catch(err => {
      console.log(err)
      this.$message.error('加载失败')
    })
  },
  methods: {
    submitForm() {
      this.ware_single_check.current_user = this.current_user
      if (this.ware_single_check.status !== 'error1') {
        this.ware_single_check.descrp.error_status = []
      }
      editDetailCheckedWare(this.ware_single_check).then(response => {
        this.$message.success('录入成功！')
        this.resetForm()
      }).catch(err => {
        this.$message.error(JSON.stringify(err.msg))
      })
    },
    resetForm() {
      this.ware_single_check = this.origin_ware_single_check
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
