<template>
  <div class="app-container">

    <!-- 查询和其他操作 -->
    <div class="filter-container">
      <el-input v-model="listQuery.name" clearable class="filter-item" style="width: 200px;" placeholder="请输入对象名称" />
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">查找</el-button>
      <el-button class="filter-item" type="primary" icon="el-icon-edit" @click="handleCreate">添加</el-button>
    </div>

    <!-- 查询结果 -->
    <el-table v-loading="listLoading" :data="list" element-loading-text="正在查询中。。。" border fit highlight-current-row>

      <el-table-column align="center" label="名称" prop="name" />

      <el-table-column align="center" label="上传时间" prop="createdtime" />

      <el-table-column align="center" label="大小(KB)" prop="size" />

      <el-table-column align="center" label="文件" width="200" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-link :href="row.url" type="success">下载</el-link>
        </template>
      </el-table-column>

      <el-table-column align="center" label="操作" width="200" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-button type="danger" size="mini" @click="handleDelete(row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

    <!-- 添加对话框 -->
    <el-dialog :visible.sync="createDialogVisible" title="上传对象">
      <el-upload ref="upload" drag :show-file-list="false" :limit="1" :http-request="handleUpload" action="#" list-type="picture">
        <i class="el-icon-upload" />
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        <div slot="tip" class="el-upload__tip">不超过2mb</div>
      </el-upload>
    </el-dialog>
  </div>
</template>

<script>
import { listAdminStorage, createAdminStorage, delAdminStorage } from '@/api/storage'
import Pagination from '@/components/Pagination'
import { mapGetters } from 'vuex' // Secondary package based on el-pagination

export default {
  name: 'Storage',
  components: { Pagination },
  data() {
    return {
      list: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 20,
        name: undefined
      },
      createDialogVisible: false,
      dataForm: {
        id: undefined,
        name: ''
      },
      updateDialogVisible: false,
      rules: {
        name: [{ required: true, message: '对象名称不能为空', trigger: 'blur' }]
      },
      downloadLoading: false,
      users: []
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      this.listQuery.owner = this.current_user === 'all' ? undefined : this.current_user

      listAdminStorage(this.listQuery).then(response => {
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
    resetForm() {
      this.dataForm = {
        id: undefined,
        name: ''
      }
    },
    handleCreate() {
      this.createDialogVisible = true
    },
    handleUpload(item) {
      this.$refs.upload.clearFiles()

      const formData = new FormData()
      formData.append('size', item.file.size)
      formData.append('name', item.file.name)
      formData.append('file', item.file)

      createAdminStorage(formData).then(response => {
        this.list.unshift(response.data)
        this.createDialogVisible = false
        this.$notify.success({
          title: '成功',
          message: '上传成功'
        })
      }).catch(err => {
        console.log(err)
        this.$message.error('上传失败，请重新上传')
      })
    },
    handleUpdate(row) {
      this.dataForm = Object.assign({}, row)
      this.updateDialogVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    handleDelete(row) {
      delAdminStorage(row.id).then(response => {
        this.$notify.success({
          title: '成功',
          message: '删除成功'
        })
        const index = this.list.indexOf(row)
        this.list.splice(index, 1)
      }).catch(err => {
        this.$notify.error({
          title: '失败',
          message: err.msg
        })
      })
    }
  }
}
</script>
