<template>
  <div class="dashboard-editor-container">

    <el-row :gutter="40" class="panel-group">
      <el-col :span="12" class="card-panel-col">
        <div class="card-panel">
          <div class="card-panel-icon-wrapper icon-people" @click="gotolink('forecastList')">
            <svg-icon icon-class="guide" class-name="card-panel-icon" />
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">预报入库数量</div>
            <count-to :start-val="0" :end-val="forecast_num" :duration="2600" class="card-panel-num" />
          </div>
        </div>
      </el-col>
      <el-col :span="12" class="card-panel-col">
        <div class="card-panel">
          <div class="card-panel-icon-wrapper icon-message" @click="gotolink('forecastList')">
            <svg-icon icon-class="guide" class-name="card-panel-icon" />
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">已入库数量</div>
            <count-to :start-val="0" :end-val="ruku_num" :duration="3000" class="card-panel-num" />
          </div>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="40" class="panel-group">
      <el-col :span="12" class="card-panel-col">
        <div class="card-panel">
          <div class="card-panel-icon-wrapper icon-money" @click="gotolink('storeList')">
            <svg-icon icon-class="chart" class-name="card-panel-icon" />
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">库存良品总数</div>
            <count-to :start-val="0" :end-val="product_good_num" :duration="3200" class="card-panel-num" />
          </div>
        </div>
      </el-col>
      <el-col :span="12" class="card-panel-col">
        <div class="card-panel">
          <div class="card-panel-icon-wrapper icon-shoppingCard" @click="gotolink('storeList')">
            <svg-icon icon-class="chart" class-name="card-panel-icon" />
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">库存废品总数</div>
            <count-to :start-val="0" :end-val="product_ungood_num" :duration="3600" class="card-panel-num" />
          </div>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="40" class="panel-group">
      <el-col :span="12" class="card-panel-col">
        <div class="card-panel">
          <div class="card-panel-icon-wrapper icon-money" @click="gotolink('chukuList')">
            <svg-icon icon-class="shopping" class-name="card-panel-icon" />
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">出库预报数量</div>
            <count-to :start-val="0" :end-val="chuku_forecast_num" :duration="3200" class="card-panel-num" />
          </div>
        </div>
      </el-col>
      <el-col :span="12" class="card-panel-col">
        <div class="card-panel">
          <div class="card-panel-icon-wrapper icon-shoppingCard" @click="gotolink('chukuList')">
            <svg-icon icon-class="shopping" class-name="card-panel-icon" />
          </div>
          <div class="card-panel-description">
            <div class="card-panel-text">已出库数量</div>
            <count-to :start-val="0" :end-val="chuku_num" :duration="3600" class="card-panel-num" />
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { fetchDashboadInfo } from '@/api/user'
import CountTo from 'vue-count-to'
import { mapGetters } from 'vuex'

export default {
  components: {
    CountTo
  },
  data() {
    return {
      forecast_num: 0,
      ruku_num: 0,
      product_good_num: 0,
      product_ungood_num: 0,
      chuku_forecast_num: 0,
      chuku_num: 0
    }
  },
  computed: {
    ...mapGetters([
      'current_user'
    ])
  },
  watch: {
    current_user: function(val) {
      this.getDashboadInfo()
    }
  },
  created() {
    this.getDashboadInfo()
  },
  methods: {
    getDashboadInfo() {
      const params = {
        user: this.current_user === 'all' ? undefined : this.current_user
      }
      fetchDashboadInfo(params).then(response => {
        this.forecast_num = response.data.forecast_num
        this.ruku_num = response.data.ruku_num
        this.product_good_num = response.data.product_good_num
        this.product_ungood_num = response.data.product_ungood_num
        this.chuku_forecast_num = response.data.chuku_forecast_num
        this.chuku_num = response.data.chuku_num
      }).catch(err => {
        this.$message.error(err.msg)
      })
    },
    gotolink(name) {
      this.$router.push({ name: name })
    }
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  .chart-wrapper {
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
  }
}

.panel-group {
  margin-top: 18px;

  .card-panel-col{
    margin-bottom: 32px;
  }
  .card-panel {
    height: 108px;
    cursor: pointer;
    font-size: 12px;
    position: relative;
    overflow: hidden;
    color: #666;
    background: #fff;
    box-shadow: 4px 4px 40px rgba(0, 0, 0, .05);
    border-color: rgba(0, 0, 0, .05);
    &:hover {
      .card-panel-icon-wrapper {
        color: #fff;
      }
      .icon-people {
         background: #40c9c6;
      }
      .icon-message {
        background: #36a3f7;
      }
      .icon-money {
        background: #f4516c;
      }
      .icon-shoppingCard {
        background: #34bfa3
      }
    }
    .icon-people {
      color: #40c9c6;
    }
    .icon-message {
      color: #36a3f7;
    }
    .icon-money {
      color: #f4516c;
    }
    .icon-shoppingCard {
      color: #34bfa3
    }
    .card-panel-icon-wrapper {
      float: left;
      margin: 14px 0 0 14px;
      padding: 16px;
      transition: all 0.38s ease-out;
      border-radius: 6px;
    }
    .card-panel-icon {
      float: left;
      font-size: 48px;
    }
    .card-panel-description {
      float: right;
      font-weight: bold;
      margin: 26px;
      margin-left: 0px;
      .card-panel-text {
        line-height: 18px;
        color: rgba(0, 0, 0, 0.45);
        font-size: 16px;
        margin-bottom: 12px;
      }
      .card-panel-num {
        font-size: 20px;
      }
    }
  }
}
</style>
