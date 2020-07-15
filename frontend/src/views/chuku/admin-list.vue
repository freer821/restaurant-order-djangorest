<template>
  <div class="app-container">

    <!-- 查询和其他操作 -->
    <div class="filter-container">
      <el-input v-model="listQuery.product_name" clearable class="filter-item" style="width: 160px;" placeholder="请输入商品名称" />
      <el-input v-model="listQuery.logistic_code" clearable class="filter-item" style="width: 160px;" placeholder="请输入快递单号" />
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">查找</el-button>
      <el-button class="filter-item" type="primary" icon="el-icon-edit" @click="handleCreate">添加</el-button>
      <el-button class="filter-item" type="primary" icon="el-icon-document" @click="handleDHLExcel(multipleSelection)">导出DHL</el-button>
    </div>

    <!-- 查询结果 -->
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="正在查询中。。。"
      border
      fit
      highlight-current-row
      :row-class-name="tableRowClassName"
      @selection-change="handleSelectionChange"
    >

      <el-table-column type="expand">
        <template slot-scope="props">
          <el-form label-position="left" class="table-expand">

            <el-form-item label="物品类型">
              <span>{{ props.row.type }}</span>
            </el-form-item>
            <el-form-item label="平台">
              <span>{{ props.row.platform }}</span>
            </el-form-item>
            <el-form-item label="负责人">
              <span>{{ props.row.contact }}</span>
            </el-form-item>
            <el-form-item label="打包类型">
              <span>{{ props.row.pack_type | parsePackType }}</span>
            </el-form-item>
            <el-form-item label="长 (cm)">
              <span>{{ props.row.long }}</span>
            </el-form-item>
            <el-form-item label="宽 (cm)">
              <span>{{ props.row.width }}</span>
            </el-form-item>
            <el-form-item label="高 (cm)">
              <span>{{ props.row.height }}</span>
            </el-form-item>
            <el-form-item label="FBA">
              <span>{{ props.row.fba_code }}</span>
            </el-form-item>

            <el-form-item label="收件人信息">
              <span>{{ props.row.reciever }}</span>
            </el-form-item>
            <el-form-item label="备注">
              <span>{{ props.row.comment }}</span>
            </el-form-item>
          </el-form>
        </template>
      </el-table-column>
      <el-table-column type="selection" align="center" />

      <el-table-column align="center" label="ID" width="80">
        <template slot-scope="{row}">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" min-width="100" label="商品名称" prop="product_name" />

      <el-table-column align="center" label="SN号" prop="sn_code" />

      <el-table-column align="center" label="快递单号" prop="logistic_code" />

      <el-table-column align="center" label="内物类型" prop="pack_content" />

      <el-table-column align="center" label="数量" prop="num" />

      <el-table-column align="center" label="出库时间" prop="sendtime" />

      <el-table-column align="center" label="状态" prop="status">
        <template slot-scope="{row}">
          <span>{{ row.status | parseStatus }}</span>
        </template>
      </el-table-column>

      <el-table-column align="center" label="创建时间" prop="createdtime" />

      <el-table-column align="center" label="操作" width="200" class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <el-button type="primary" size="mini" @click="handleUpdate(scope.row)">编辑</el-button>
          <el-button type="danger" size="mini" @click="handleDelete(scope.row)">删除</el-button>
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
  .el-table .warning-row {
    background: oldlace;
  }
</style>

<script>
import { listAdminChuku, delAdminChuku } from '@/api/chuku'
import BackToTop from '@/components/BackToTop'
import Pagination from '@/components/Pagination' // Secondary package based on el-pagination
import { mapGetters } from 'vuex' // Secondary package based on el-pagination

export default {
  name: 'ForecastsList',
  components: { BackToTop, Pagination },
  filters: {
    parseStatus(status) {
      const statusMap = {
        created: '已创建',
        handled: '处理中',
        finished: '完成'
      }
      return statusMap[status]
    },
    parsePackType(type) {
      const typeMap = {
        pallet: '托盘',
        carton: '纸箱'
      }
      return typeMap[type]
    }
  },
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
      downloadLoading: false,
      multipleSelection: [],
      tableHeader: ['Dingdanhao', 'Name 1', 'Name 2, Postnummer', 'Name 3', 'Emp.Tel', 'Street', 'Nr.', 'country', 'PLZ',
        'City', 'fd', 'Gewicht', 'No. of Floor or Appartment', 'Mark2', 'Mark3', 'ShipperName', 'ShipperCompany', 'ShipperAddress', 'Menpai',
        'ShipperZipCode', 'ShipperCity', 'Rg.Nr', 'Service']
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
    console.log(this.$store.getters.token)
  },
  methods: {
    tableRowClassName({ row, rowIndex }) {
      return ''
    },
    getList() {
      this.listLoading = true
      this.listQuery.offset = (this.listQuery.page - 1) * this.listQuery.limit
      this.listQuery.owner = this.current_user === 'all' ? undefined : this.current_user

      listAdminChuku(this.listQuery).then(response => {
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
      this.$router.push({ path: '/admin/chuku/create' })
    },
    handleUpdate(row) {
      this.$router.push({ path: '/admin/chuku/edit', query: { id: row.id }})
    },
    handleDelete(row) {
      this.$confirm('此操作将永久删除该选项, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        delAdminChuku(row.id).then(response => {
          this.$message.success('删除成功！')
        }).catch(err => {
          this.$message.error('删除失败！' + JSON.stringify(err.msg))
        })
        this.$router.push({ path: '/admin/chuku/list' })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    handleDHLExcel() {
      if (this.multipleSelection.length === 0) {
        this.$message.error('请选择至少一条记录')
      } else {
        import('@/vendor/Export2Excel').then(excel => {
          const filterVal = ['Dingdanhao', 'reciever_name', 'name2', 'reciever_extra', 'reciever_tel', 'reciever_addr',
            'reciever_housenr', 'reciever_country', 'reciever_postcode', 'reciever_city',
            'fd', 'weight', 'Floor', 'Mark2', 'Mark3', 'ShipperName', 'ShipperCompany', 'ShipperAddress', 'Menpai',
            'ShipperZipCode', 'ShipperCity', 'Rg_Nr', 'Service']
          const chuku_arr = []
          for (let i = 0; i < this.multipleSelection.length; i++) {
            const selected_chuku = this.multipleSelection[i]
            const chuku = {
              Dingdanhao: '',
              reciever_name: selected_chuku.reciever.name,
              name2: selected_chuku.reciever.name,
              reciever_extra: selected_chuku.reciever.extra,
              reciever_tel: selected_chuku.reciever.tel,
              reciever_addr: selected_chuku.reciever.addr,
              reciever_housenr: selected_chuku.reciever.housenr,
              reciever_country: selected_chuku.reciever.country,
              reciever_postcode: selected_chuku.reciever.postcode,
              reciever_city: selected_chuku.reciever.city,
              fd: '',
              weight: selected_chuku.weight,
              Floor: '',
              Mark2: '',
              Mark3: '',
              ShipperName: 'Dongliang',
              ShipperCompany: 'i.A.v. Team C',
              ShipperAddress: 'Waldstr',
              Menpai: '23/D7',
              ShipperZipCode: '63128',
              ShipperCity: 'Dietzenbach',
              Rg_Nr: '',
              Service: ''
            }
            chuku_arr.push(chuku)
          }
          excel.export_json_to_excel2(this.tableHeader, chuku_arr, filterVal, 'DHL模板')
        })
      }
    },
    handleSelectionChange(val) {
      this.multipleSelection = val
    }
  }
}
</script>
