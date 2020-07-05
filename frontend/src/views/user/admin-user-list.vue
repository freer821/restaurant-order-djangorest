<template>
  <div class="app-container">

    <!-- 查询和其他操作 -->
    <div class="filter-container">
      <el-input v-model="listQuery.username" clearable class="filter-item" style="width: 200px;" placeholder="请输入用户名" />
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">查找</el-button>
    </div>

    <!-- 查询结果 -->
    <el-table v-loading="listLoading" :data="list" element-loading-text="正在查询中。。。" border fit highlight-current-row>
      <el-table-column align="center" width="100px" label="用户ID" prop="id" sortable />

      <el-table-column align="center" label="用户名" prop="username" />

      <el-table-column align="center" label="状态" prop="is_active">
        <template slot-scope="scope">
          <el-tag>{{ scope.row.is_active | parseStatus }}</el-tag>
        </template>
      </el-table-column>

      <el-table-column align="center" label="加入时间" prop="date_joined" />

      <el-table-column align="center" label="最后登录" prop="last_login" />

      <el-table-column align="center" label="公司" prop="profile.company_name" />
      <el-table-column align="center" label="电话" prop="profile.company_tel" />
      <el-table-column align="center" label="地址" prop="profile.company_addr" />

    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

  </div>
</template>

<script>
import { fetchUserListAdmin } from '@/api/user'
import Pagination from '@/components/Pagination' // Secondary package based on el-pagination

export default {
  name: 'User',
  components: { Pagination },
  filters: {
    parseStatus(status) {
      if (status) {
        return '已激活'
      }
      return '未激活'
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
      list: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 20,
        offset: 0,
        username: undefined
      },
      downloadLoading: false,
      genderDic: ['未知', '男', '女'],
      levelDic: ['普通用户', 'VIP用户', '高级VIP用户'],
      statusDic: ['可用', '禁用', '注销']
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      this.listQuery.offset = (this.listQuery.page - 1) * this.listQuery.limit
      fetchUserListAdmin(this.listQuery).then(response => {
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
    }
  }
}
</script>
