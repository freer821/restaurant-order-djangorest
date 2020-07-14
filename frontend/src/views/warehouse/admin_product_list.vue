<template>
  <div class="app-container">
    <el-card class="box-card">
      <h3>商品名称 - {{ title }}</h3>
      <!-- 查询和其他操作 -->
      <div class="filter-container">
        <el-input v-model="listQuery.sn_code" clearable class="filter-item" style="width: 160px;" placeholder="请输入SN码" />
        <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">查找</el-button>
      </div>

      <!-- 查询结果 -->
      <el-table v-loading="listLoading" :data="list" element-loading-text="正在查询中。。。" border fit highlight-current-row>
        <el-table-column align="center" label="ID" width="80">
          <template slot-scope="{row}">
            <span>{{ row.id }}</span>
          </template>
        </el-table-column>
        <el-table-column align="center" min-width="100" label="SN码" prop="sn_code" />
        <el-table-column align="center" min-width="100" label="状态" prop="status">
          <template slot-scope="{row}">
            <span>{{ row.status | parseStatus }}</span>
          </template>

        </el-table-column>
        <el-table-column align="center" min-width="100" label="维修记录">
          <template slot-scope="{row}">
            <span>{{ row.descrp.repair_record | parseRecordStatus }}</span>
          </template>
        </el-table-column>
        <el-table-column align="center" min-width="100" label="备注" prop="descrp.comment" />
        <el-table-column align="center" min-width="100" label="操作时间" prop="operation_time" />

        <el-table-column align="center" label="操作" class-name="small-padding fixed-width">
          <template slot-scope="{row}">
            <el-button type="primary" size="small" @click="handleUpdate(row)">编辑</el-button>
          </template>
        </el-table-column>
      </el-table>

      <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

      <el-tooltip placement="top" content="返回顶部">
        <back-to-top :visibility-height="100" />
      </el-tooltip>
    </el-card>
  </div>
</template>

<style>
  .table-expand label {
    width: 100px;
    color: #99a9bf;
  }
  .table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
  }
  .gallery {
    width: 80px;
    margin-right: 10px;
  }
  .goods-detail-box img {
    width: 100%;
  }
</style>

<script>
import { getAdminDetailCheckedWares } from '@/api/warehouse'
import BackToTop from '@/components/BackToTop/index'
import Pagination from '@/components/Pagination/index'

export default {
  name: 'AdminWarehouseDetailList',
  components: { BackToTop, Pagination },
  filters: {
    parseRecordStatus(status) {
      const statusMap = {
        software: '软件',
        hardware: '硬件'
      }
      const statustranslate = status.map(s => statusMap[s])

      return statustranslate.join(', ')
    },
    parseStatus(status) {
      const statusMap = {
        normal: '良品',
        error0: '划痕',
        error1: '故障'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      title: '',
      list: [],
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 20,
        offset: 0,
        sn_code: undefined,
        product_name: undefined
      },
      downloadLoading: false
    }
  },
  watch: {
    current_user: function(val) {
      this.getList()
    }
  },
  mounted() {
    this.title = this.$route.query.title
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      this.listQuery.warehouse = this.$route.query.warehouse
      this.listQuery.offset = (this.listQuery.page - 1) * this.listQuery.limit
      console.log(this.listQuery)
      getAdminDetailCheckedWares(this.listQuery).then(response => {
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      }).catch(() => {
        this.list = []
        this.total = 0
        this.listLoading = false
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    handleUpdate(row) {
      this.$router.push({ path: '/admin/warehouse/checkdetail', query: { id: row.id }})
    }
  }
}
</script>
