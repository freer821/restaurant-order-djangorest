<template>
  <div class="app-container">

    <!-- 查询和其他操作 -->
    <div class="filter-container">
      <el-input v-model="listQuery.product_name" clearable class="filter-item" style="width: 160px;" placeholder="请输入商品名称" />
      <el-input v-model="listQuery.logistic_code" clearable class="filter-item" style="width: 160px;" placeholder="请输入快递单号" />
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">查找</el-button>
      <el-button class="filter-item" type="primary" icon="el-icon-edit" @click="handleCreate">添加</el-button>
    </div>

    <!-- 查询结果 -->
    <el-table v-loading="listLoading" :data="list" element-loading-text="正在查询中。。。" border fit highlight-current-row>

      <el-table-column type="expand">
        <template slot-scope="props">
          <el-form label-position="left" class="table-expand">
            <el-form-item label="商品ID">
              <span>{{ props.row.extra.orderID }}</span>
            </el-form-item>
            <el-form-item label="平台">
              <span>{{ props.row.extra.platform }}</span>
            </el-form-item>
            <el-form-item label="发件人信息">
              <span>{{ props.row.extra.sender }}</span>
            </el-form-item>
            <el-form-item label="备注">
              <span>{{ props.row.extra.comment }}</span>
            </el-form-item>
            <el-form-item label="管理员备注">
              <span>{{ props.row.extra.admin_extra }}</span>
            </el-form-item>
          </el-form>
        </template>
      </el-table-column>

      <el-table-column align="center" min-width="100" label="商品名称" prop="product_name" />

      <el-table-column align="center" min-width="150" label="快递单号" prop="logistic_code" />

      <el-table-column align="center" label="快递公司" prop="logistic_company" />

      <el-table-column align="center" label="维修仓出标签" prop="status">
        <template slot-scope="scope">
          <el-tag :type="scope.row.extra.isLabeledByStore ? 'success' : 'error' ">{{ scope.row.extra.isLabeledByStore ? '是' : '否' }}</el-tag>
        </template>
      </el-table-column>

      <el-table-column align="center" label="预报数量" prop="expected_num" />

      <el-table-column align="center" label="入库数量" prop="real_num" />

      <el-table-column align="center" label="预报时间" prop="createdtime" />

      <el-table-column align="center" label="入库时间" prop="arrivedtime" />

      <el-table-column align="center" label="操作" width="200" class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <el-button type="primary" size="mini" @click="handleUpdate(scope.row)">编辑</el-button>
          <el-button v-if="!scope.row.arrivedtime" type="danger" size="mini" @click="handleDelete(scope.row)">删除</el-button>
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
  .table-expand {
    font-size: 0;
  }
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
import { listForecasts } from '@/api/forecast'
import BackToTop from '@/components/BackToTop'
import Pagination from '@/components/Pagination' // Secondary package based on el-pagination

export default {
  name: 'ForecastsList',
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
        product_name: undefined,
        logistic_code: undefined
      },
      goodsDetail: '',
      detailDialogVisible: false,
      downloadLoading: false
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      this.listQuery.offset = (this.listQuery.page - 1) * this.listQuery.limit
      listForecasts(this.listQuery).then(response => {
        console.log(response.data)
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
    handleCreate() {
      this.$router.push({ path: '/forecast/single-create' })
    },
    handleUpdate(row) {
      this.$router.push({ path: '/forecast/edit', query: { id: row.id }})
    },
    showDetail(detail) {
      this.goodsDetail = detail
      this.detailDialogVisible = true
    },
    handleDelete(row) {

    }
  }
}
</script>
