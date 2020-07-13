<template>
  <div class="app-container">

    <el-card class="box-card">
      <h3>检修</h3>
      <el-radio-group v-model="check_type" style="padding: 20px">
        <el-radio-button label="massiv"> 批量录入</el-radio-button>
        <el-radio-button label="single"> 详细录入</el-radio-button>
      </el-radio-group>
      <el-form v-if="check_type==='massiv'" ref="ware_massiv_check" :model="ware_massiv_check" label-width="150px">
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
      <el-form v-else ref="ware_single_check" :model="ware_single_check" label-width="150px">
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
        <el-form-item v-show="ware_single_check.status==='normal'" label="维修记录" prop="repair_record">
          <el-checkbox-group v-model="ware_single_check.descrp.repair_record">
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
        <el-form-item label="操作时间" prop="operation_time">
          <el-date-picker
            v-model="ware_single_check.operation_time"
            type="datetime"
            placeholder="选择日期"
            default-time="12:00:00"
          />
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
import { pushMassivCheckedWares, pushDetailCheckedWares } from '@/api/warehouse'

import { mapGetters } from 'vuex'
export default {
  name: 'WarehouseCheck',

  data() {
    return {
      ware_massiv_check: {
        product_name: '',
        num: '',
        status: 'normal'
      },
      ware_single_check: {
        product_name: '',
        status: 'normal',
        sn_code: '',
        descrp: {
          comment: '',
          repair_record: []
        },
        operation_time: ''
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
      if (this.current_user !== 'all') {
        if (this.check_type === 'massiv') {
          this.ware_massiv_check.current_user = this.current_user
          pushMassivCheckedWares(this.ware_massiv_check).then(response => {
            this.$message.success('录入成功！')
            this.resetForm()
          }).catch(err => {
            this.$message.error(err.msg)
          })
        } else {
          this.ware_single_check.current_user = this.current_user
          pushDetailCheckedWares(this.ware_single_check).then(response => {
            this.$message.success('录入成功！')
            this.resetForm()
          }).catch(err => {
            this.$message.error(JSON.stringify(err.msg))
          })
        }
      } else {
        this.$message.error('请先选择操作客户！')
        return false
      }
    },
    resetForm() {
      this.ware_massiv_check = {
        product_name: '',
        num: '',
        status: 'normal'
      }
      this.ware_single_check = {
        product_name: '',
        status: 'normal',
        sn_code: '',
        descrp: {
          comment: '',
          repair_record: []
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
