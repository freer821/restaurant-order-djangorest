<template>
  <div class="app-container">

    <!-- 查询和其他操作 -->
    <div class="filter-container">
      <el-input v-model="listQuery.product_name" clearable class="filter-item" style="width: 160px;" placeholder="请输入商品名称" />
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">查找</el-button>
    </div>

    <!-- 查询结果 -->
    <el-table v-loading="listLoading" :data="list" element-loading-text="正在查询中。。。" border fit show-summary highlight-current-row>
      <el-table-column align="center" label="ID" width="80">
        <template slot-scope="{row}">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" min-width="100" label="商品名称" prop="product_name" />

      <el-table-column align="center" label="待操作" prop="unknown_num">
        <template slot-scope="{row}">
          <template v-if="row.edit">
            <el-input v-model="row.unknown_num" class="edit-input" size="small" />

          </template>
          <span v-else>{{ row.unknown_num }}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="良品" prop="normal_num">
        <template slot-scope="{row}">
          <template v-if="row.edit">
            <el-input v-model="row.normal_num" class="edit-input" size="small" />

          </template>
          <span v-else>{{ row.normal_num }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="废品">
        <el-table-column align="center" label="划痕" prop="error0_num">
          <template slot-scope="{row}">
            <template v-if="row.edit">
              <el-input v-model="row.error0_num" class="edit-input" size="small" />

            </template>
            <span v-else>{{ row.error0_num }}</span>
          </template>
        </el-table-column>

        <el-table-column align="center" label="故障" prop="error1_num">
          <template slot-scope="{row}">
            <template v-if="row.edit">
              <el-input v-model="row.error1_num" class="edit-input" size="small" />

            </template>
            <span v-else>{{ row.error1_num }}</span>
          </template>
        </el-table-column>
      </el-table-column>

      <el-table-column align="center" label="操作" width="300" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-button
            v-show="row.edit"
            class="cancel-btn"
            size="mini"
            icon="el-icon-refresh"
            type="warning"
            @click="cancelEdit(row)"
          >
            cancel
          </el-button>
          <el-button
            v-if="row.edit"
            type="success"
            size="mini"
            icon="el-icon-circle-check-outline"
            @click="confirmEdit(row)"
          >
            Ok
          </el-button>
          <el-button
            v-else
            type="primary"
            size="mini"
            icon="el-icon-edit"
            @click="row.edit=!row.edit"
          >
            编辑
          </el-button>
          <el-button v-show="row.product_count > 0" type="primary" size="mini" @click="handleDetail(row)">详情</el-button>
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
import { getAdminWarehouseList, updateAdminWarehouseList } from '@/api/warehouse'
import BackToTop from '@/components/BackToTop'
import Pagination from '@/components/Pagination'
import { mapGetters } from 'vuex' // Secondary package based on el-pagination
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
        owner: undefined,
        product_name: undefined
      },
      goodsDetail: '',
      detailDialogVisible: false,
      downloadLoading: false,
      ware_detail_list: {
        title: '',
        show: false
      }
    }
  },
  computed: {
    ...mapGetters([
      'current_user'
    ])
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
      getAdminWarehouseList(this.listQuery).then(response => {
        const items = response.data.results
        this.list = items.map(v => {
          this.$set(v, 'edit', false) // https://vuejs.org/v2/guide/reactivity.html
          v.unknown_num_original = v.unknown_num
          v.normal_num_original = v.normal_num
          v.error0_num_original = v.error0_num
          v.error1_num_original = v.error1_num
          return v
        })
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
    cancelEdit(row) {
      row.edit = false
      row.unknown_num = row.unknown_num_original
      row.normal_num = row.normal_num_original
      row.error0_num = row.error0_num_original
      row.error1_num = row.error1_num_original

      this.$message({
        message: '放弃修改',
        type: 'warning'
      })
    },
    confirmEdit(row) {
      row.edit = false
      const submitObject = JSON.parse(JSON.stringify(row))
      delete submitObject.edit
      delete submitObject.unknown_num_original
      delete submitObject.normal_num_original
      delete submitObject.error0_num_original
      delete submitObject.error1_num_original

      updateAdminWarehouseList(submitObject).then(reponse => {
        row.unknown_num_original = row.unknown_num
        row.normal_num_original = row.normal_num
        row.error0_num_original = row.error0_num
        row.error1_num_original = row.error1_num

        this.$message({
          message: '更新成功！',
          type: 'success'
        })
      }).catch(err => {
        this.$message({
          message: '更新失败：' + err.msg,
          type: 'error'
        })
      })
    },
    handleDetail(row) {
      this.$router.push({ path: '/admin/warehouse/product', query: { warehouse: row.id, title: row.product_name }})
    }

  }
}
</script>
