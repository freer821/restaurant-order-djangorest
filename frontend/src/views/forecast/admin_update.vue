<template>
  <div class="app-container">

    <el-card class="box-card">
      <h3>预报更新</h3>
      <el-form ref="forecast" :rules="rules" :model="forecast" label-width="150px">
        <el-form-item label="快递单号" prop="logistic_code">
          <el-input v-model="forecast.logistic_code" disabled />
        </el-form-item>
        <el-form-item label="产品名称" prop="product_name">
          <el-input v-model="forecast.product_name" disabled />
        </el-form-item>
        <el-form-item
          label="入库数量"
          prop="real_num"
        >
          <el-input v-model="forecast.real_num" type="number" placeholder="0" />
        </el-form-item>
        <el-form-item label="SN码">
          <el-input v-model="forecast.admin_extra.sn_codes" type="textarea" :rows="2" placeholder="多个SN码，中间以英文逗号(,)隔开" />
        </el-form-item>
        <el-form-item label="PLN码">
          <el-input v-model="forecast.admin_extra.pln_codes" type="textarea" :rows="2" placeholder="多个PLN码，中间以英文逗号(,)隔开" />
        </el-form-item>
        <el-form-item label="入库时间" prop="arrivedtime">
          <el-date-picker
            v-model="forecast.arrivedtime"
            type="datetime"
            placeholder="选择日期"
            default-time="12:00:00"
          />
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
import { getForecastAdmin, updateForecastAdmin } from '@/api/forecast'
import { mapGetters } from 'vuex'
export default {
  name: 'RukuHandle',

  data() {
    return {
      origin_forecast: {
      },
      forecast: {
      },
      rules: {
        product_name: [{ required: true, message: '产品名称不能为空', trigger: 'blur' }],
        real_num: [
          { required: true, message: '不能为空或非数字', trigger: 'blur' }
        ],
        logistic_code: [{ required: true, message: '快递单号不能为空', trigger: 'blur' }],
        arrivedtime: [{ required: true, message: '入库时间不能为空', trigger: 'blur' }]
      }
    }
  },
  computed: {
    ...mapGetters([
      'current_user'
    ])
  },
  created() {
    getForecastAdmin(this.$route.query.id).then(respone => {
      this.forecast = respone.data
      this.origin_forecast = Object.assign({}, this.chuku)
    }).catch(err => {
      console.log(err)
      this.$message.error('加载失败')
    })
  },

  methods: {
    submitForm() {
      this.$refs.forecast.validate((valid) => {
        if (valid) {
          updateForecastAdmin(this.forecast).then(response => {
            this.$confirm('更新成功', '预报入库', {
              confirmButtonText: '前往预报列表',
              cancelButtonText: '继续添加'
            }).then(() => {
              this.$router.push('list')
            }).catch(() => {
              this.resetForm()
            })
          }).catch(err => {
            this.$notify.error('添加失败： ' + JSON.stringify(err.msg))
          })
        } else {
          this.$message.error('请检查输入，并查看当前操作用户是否正确！')
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
