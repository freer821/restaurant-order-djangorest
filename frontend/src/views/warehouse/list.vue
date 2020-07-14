<template>
  <div class="app-container">

    <!-- 查询和其他操作 -->
    <div class="filter-container">
      <el-input v-model="listQuery.product_name" clearable class="filter-item" style="width: 160px;" placeholder="请输入商品名称" />
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">查找</el-button>
    </div>

    <!-- 查询结果 -->
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="正在查询中。。。"
      border
      fit
      show-summary
      highlight-current-row
    >

      <el-table-column align="center" min-width="100" label="商品名称" prop="product_name" />

      <el-table-column align="center" label="待操作" prop="unknown_num" />
      <el-table-column align="center" label="良品" prop="normal_num" />

      <el-table-column align="center" label="废品">
        <el-table-column align="center" label="划痕" prop="error0_num" />

        <el-table-column align="center" label="故障" prop="error1_num" />
      </el-table-column>
      <el-table-column align="center" label="操作" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-button v-show="row.product_count > 0" type="primary" size="small" @click="handleDetail(row)">详情</el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

    <el-tooltip placement="top" content="返回顶部">
      <back-to-top :visibility-height="100" />
    </el-tooltip>
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
import { getUserWarehouseList } from '@/api/warehouse'
import BackToTop from '@/components/BackToTop'
import Pagination from '@/components/Pagination'
export default {
  name: 'WarehouseList',
  components: { BackToTop, Pagination },
  data() {
    return {
      list: [],
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 20,
        offset: 0,
        product_name: undefined
      },
      downloadLoading: false,
      ware_detail_list: {
        title: '',
        show: false
      },
      multipleSelection: []
    }
  },
  watch: {
    current_user: function(val) {
      this.getList()
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      this.listQuery.offset = (this.listQuery.page - 1) * this.listQuery.limit
      this.listQuery.owner = this.current_user === 'all' ? undefined : this.current_user
      getUserWarehouseList(this.listQuery).then(response => {
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
    handleDetail(row) {
      this.$router.push({ path: '/warehouse/product', query: { warehouse: row.id, title: row.product_name }})
    }
  }
}
</script>
