<template>
  <div class="app-container">

    <el-card class="box-card">
      <h3>入库预报</h3>
      <el-form ref="forecast" :rules="rules" :model="forecast" label-width="150px">
        <el-form-item label="快递单号" prop="logistic_code">
          <el-input v-model="forecast.logistic_code" />
        </el-form-item>
        <el-form-item label="产品名称" prop="product_name">
          <el-input v-model="forecast.product_name" />
        </el-form-item>
        <el-form-item
          label="预报数量"
          prop="expected_num"
        >
          <el-input v-model="forecast.expected_num" type="number" placeholder="0" />
        </el-form-item>
        <el-form-item label="快递公司">
          <el-input v-model="forecast.logistic_company" />
        </el-form-item>
        <el-form-item label="是否由维修仓出标签">
          <el-radio-group v-model="forecast.extra.isLabeledByStore">
            <el-radio :label="true">是</el-radio>
            <el-radio :label="false">否</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="订单号">
          <el-input v-model="forecast.extra.orderID" />
        </el-form-item>
        <el-form-item label="负责人">
          <el-input v-model="forecast.extra.contact" />
        </el-form-item>
        <el-form-item label="平台">
          <el-input v-model="forecast.extra.platform" />
        </el-form-item>
        <el-form-item label="发货人">
          <el-input v-model="forecast.extra.sender.name" />
        </el-form-item>
        <el-form-item label="街道名 街道号">
          <el-input v-model="forecast.extra.sender.addr" />
        </el-form-item>
        <el-form-item label="城市">
          <el-input v-model="forecast.extra.sender.city" />
        </el-form-item>
        <el-form-item label="邮编">
          <el-input v-model="forecast.extra.sender.postcode" />
        </el-form-item>
        <el-form-item label="发货国">
          <el-input v-model="forecast.extra.sender.country" />
        </el-form-item>
        <el-form-item label="备注">
          <el-input v-model="forecast.extra.comment" type="textarea" :rows="2" placeholder="请输入内容" />
        </el-form-item>
      </el-form>
    </el-card>
    <div v-if="!forecast.arrivedtime" class="op-container">
      <el-button @click="resetForm">恢复</el-button>
      <el-button type="primary" @click="submitForm">修改</el-button>
    </div>
  </div>
</template>

<script>
import { getForecast, editForecast } from '@/api/forecast'
export default {
  name: 'RukuEdit',

  data() {
    return {
      forecast: {
        logistic_code: '',
        logistic_company: '',
        product_name: '',
        status: '',
        expected_num: '',
        extra: {
          isLabeledByStore: false,
          orderID: '',
          comment: '',
          contact: '',
          platform: '',
          sender: {
            name: '',
            addr: '',
            city: '',
            postcode: '',
            country: ''
          }
        }
      },
      origin_forecast: {},
      rules: {
        product_name: [{ required: true, message: '产品名称不能为空', trigger: 'blur' }],
        expected_num: [
          { required: true, message: '不能为空或非数字', trigger: 'blur' }
        ],
        logistic_code: [{ required: true, message: '快递单号不能为空', trigger: 'blur' }]
      }
    }
  },
  created() {
    getForecast(this.$route.query.id).then(respone => {
      this.origin_forecast = respone.data
      this.forecast = this.origin_forecast
    }).catch(err => {
      console.log(err)
      this.$message.error('加载失败')
    })
  },
  methods: {
    submitForm() {
      this.$refs.forecast.validate((valid) => {
        if (valid) {
          editForecast(this.forecast).then(response => {
            this.$confirm('修改成功', '修改预报', {
              confirmButtonText: '返回预报列表'
            }).then(() => {
              this.$router.push('forecastList')
            })
          }).catch(err => {
            this.$notify.error('修改失败： ' + JSON.stringify(err.msg))
          })
        } else {
          this.$message.error('输入有误，请检查！')
          return false
        }
      })
    },
    resetForm() {
      this.forecast = this.origin_forecast
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
