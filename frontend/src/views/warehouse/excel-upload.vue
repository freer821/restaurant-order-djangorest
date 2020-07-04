<template>
  <div class="app-container">
    <div class="filter-container">
      <el-button :loading="downloadLoading" class="filter-item" type="primary" icon="el-icon-download" @click="handleDownload">下载预报EXCEL模板</el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
        提交
      </el-button>
    </div>

    <upload-excel-component :on-success="handleSuccess" :before-upload="beforeUpload" />
    <el-table :data="tableData" border highlight-current-row style="width: 100%;margin-top:20px;">
      <el-table-column v-for="item of tableHeader" :key="item" :prop="item" :label="item" />
    </el-table>
  </div>
</template>

<script>
import UploadExcelComponent from '@/components/UploadExcel/index.vue'
import { addForecast } from '@/api/forecast'

export default {
  name: 'ExcelUpload',
  components: { UploadExcelComponent },
  data() {
    return {
      downloadLoading: false,
      tableData: [],
      tableHeader: ['快递单号*', '商品名称*', '预报发货数量*', '快递公司', '是否由维修仓出标签(是/否)', '订单号', '负责人', '平台', '发货人',
        '街道名 街道号', '城市', '邮编', '发货国', '备注'],

      submitData: []
    }
  },
  methods: {
    beforeUpload(file) {
      const isLt1M = file.size / 1024 / 1024 < 1

      if (isLt1M) {
        return true
      }

      this.$message({
        message: 'Please do not upload files larger than 1m in size.',
        type: 'warning'
      })
      return false
    },
    handleSuccess({ results, header }) {
      this.tableData = results
      this.submitData = results.map(v => this.tableHeader.map(j => {
        if (j === '是否由维修仓出标签(是/否)') {
          if (v[j] && v[j].includes('是')) {
            v[j] = '是'
          } else {
            v[j] = '否'
          }
        }
        return v[j]
      }))
    },
    handleCreate() {
      if (this.submitData.length === 0) {
        this.$message.error('未发现可提交的数据！')
      } else if (this.checkSubmitData()) {
        const loading = this.$loading({
          lock: true,
          text: 'Loading',
          spinner: 'el-icon-loading',
          background: 'rgba(0, 0, 0, 0.7)'
        })

        const error_forecasts = []

        for (let i = 0; i < this.submitData.length; i++) {
          const forecast = {
            logistic_code: this.submitData[i][0],
            product_name: this.submitData[i][1],
            expected_num: this.submitData[i][2],
            logistic_company: this.submitData[i][3],
            status: '0',
            extra: {
              isLabeledByStore: this.submitData[i][4] === '是',
              orderID: this.submitData[i][5],
              contact: this.submitData[i][6],
              platform: this.submitData[i][7],
              sender: {
                name: this.submitData[i][8],
                addr: this.submitData[i][9],
                city: this.submitData[i][10],
                postcode: this.submitData[i][11],
                country: this.submitData[i][12]
              },
              comment: this.submitData[i][13]
            }
          }
          addForecast(forecast).then(response => {
            loading.$message.success('第 ' + i + ' 条数据提交成功！')
          }).catch(err => {
            loading.$message.error('第 ' + i + ' 条数据提交失败: ' + JSON.stringify(err.msg))
            error_forecasts.push([...this.submitData[i], err.msg])
          }).finally(() => {
            loading.close()
            if (error_forecasts.length > 0) {
              this.handleErrorDownload(error_forecasts)
            }
          })
        }
      }
    },
    checkSubmitData() {
      for (let i = 0; i < this.submitData.length; i++) {
        if (!this.submitData[i][0] || !this.submitData[i][2]) {
          this.$message.error('录入数据有错误，快递单号，产品名称不能为空， 请检查后重新上传！')
          return false
        }

        if (!isNaN(parseFloat(this.submitData[i][3]))) {
          this.$message.error('录入数据有错误，预报数量不是数字， 请检查后重新上传！')
          return false
        }
      }
      return true
    },
    handleDownload() {
      this.downloadLoading = true
      import('@/vendor/Export2Excel').then(excel => {
        const filterVal = ['logistic_code', 'product_name', 'expected_num', 'logistic_company', 'isLabeledByStore', 'orderID',
          'contact', 'platform', 'sender_name', 'sender_addr', 'sender_city', 'sender_country', 'sender_postcode', 'comment']
        const forecasts = [{
          logistic_code: '',
          logistic_company: '',
          product_name: '',
          expected_num: '',
          isLabeledByStore: '',
          orderID: '',
          contact: '',
          platform: '',
          sender_name: '',
          sender_addr: '',
          sender_city: '',
          sender_country: '',
          sender_postcode: '',
          comment: ''
        }]

        excel.export_json_to_excel2(this.tableHeader, forecasts, filterVal, '预报EXCEL模板')
        this.downloadLoading = false
      })
    },
    handleErrorDownload(data) {
      import('@/vendor/Export2Excel').then(excel => {
        excel.export_json_to_excel({ header: [...this.tableHeader, '错误原因'], data, filename: '预报导入错误明细' })
      })
    }

  }
}
</script>
