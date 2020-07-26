<template>
  <div class="app-container">

    <el-card class="box-card">
      <h3>商品 -  {{ title }}</h3>
      <el-form ref="good" :rules="rules" :model="good" label-width="150px">
        <el-form-item label="所属分类" prop="category">
          <el-select
            v-model="good.category"
            clearable
            placeholder="请选择"
          >
            <el-option
              v-for="item in categories"
              :key="item.id"
              :label="item.name"
              :value="item.id"
            />
          </el-select>
        </el-form-item>

        <el-form-item label="产品名称" prop="name">
          <el-input v-model="good.name" />
        </el-form-item>
        <el-form-item label="价格" prop="price">
          <el-input v-model="good.price" />
        </el-form-item>
        <el-form-item label="每天数量" prop="day_limit">
          <el-input v-model="good.day_limit" />
        </el-form-item>

        <el-form-item label="商品图片">
          <el-upload
            :http-request="uploadImg"
            :show-file-list="false"
            class="avatar-uploader"
            accept=".jpg,.jpeg,.png,.gif"
          >
            <img v-if="good.content.img" :src="good.content.img" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon" />

          </el-upload>
        </el-form-item>
        <el-form-item label="是否启用">
          <el-radio-group v-model="good.isactived">
            <el-radio :label="true">是</el-radio>
            <el-radio :label="false">否</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="配料">
          <json-editor ref="jsonEditor" v-model="good.content.extra" />
        </el-form-item>
      </el-form>
    </el-card>
    <div class="op-container">
      <el-button @click="resetForm">恢复</el-button>
      <el-button type="primary" @click="submitForm">修改</el-button>
    </div>
  </div>
</template>

<script>
import JsonEditor from './components/jsoneditor'

import { createAdminStorage } from '@/api/storage'

import { getGoodAdmin, updateGoodAdmin, createGoodAdmin } from '@/api/good'
import { listAdmincategory } from '@/api/category'
export default {
  name: 'GoodCreateOrEdit',
  components: { JsonEditor },
  data() {
    return {
      title: '',
      good: {
        name: '',
        category: '',
        price: '',
        day_limit: '',
        isactived: true,
        content: {
          img: '',
          extra: {}
        }
      },
      categories: [],
      origin_good: {},
      rules: {
        category: [{ required: true, message: '产品分类不能为空', trigger: 'blur' }],
        name: [{ required: true, message: '产品名称不能为空', trigger: 'blur' }],
        price: [{ required: true, message: '产品价格不能为空', trigger: 'blur' }],
        day_limit: [{ required: true, message: '产品名称不能为空', trigger: 'blur' }]

      }
    }
  },
  created() {
    if (this.$route.query.id) {
      getGoodAdmin(this.$route.query.id).then(respone => {
        this.good = respone.data
        this.good.content.extra = JSON.parse(this.good.content.extra)
        this.title = this.good.name
        this.origin_good = Object.assign({}, this.good)
      }).catch(err => {
        console.log(err)
        this.$message.error('加载失败')
      })
    } else {
      this.title = '新建'
    }

    listAdmincategory().then(response => {
      this.categories = response.data.results
      console.log(this.categories)
      this.listLoading = false
    }).catch(() => {
    })
  },
  methods: {
    submitForm() {
      this.$refs.good.validate((valid) => {
        if (valid) {
          if (!this.$route.query.id) {
            createGoodAdmin(this.good).then(response => {
              this.$confirm('新建成功', '新建商品', {
                confirmButtonText: '返回商品列表'
              }).then(() => {
                this.$router.push('list')
              })
            }).catch(err => {
              this.$notify.error('新建失败： ' + JSON.stringify(err.msg))
            })
          } else {
            updateGoodAdmin(this.good).then(response => {
              this.$confirm('修改成功', '修改商品', {
                confirmButtonText: '返回商品列表'
              }).then(() => {
                this.$router.push('list')
              })
            }).catch(err => {
              this.$notify.error('修改失败： ' + JSON.stringify(err.msg))
            })
          }
        } else {
          this.$message.error('输入有误，请检查！')
          return false
        }
      })
    },
    resetForm() {
      this.good = this.origin_good
    },
    uploadImg(item) {
      const formData = new FormData()
      formData.append('size', item.file.size)
      formData.append('name', item.file.name)
      formData.append('file', item.file)

      createAdminStorage(formData).then(response => {
        this.good.content.img = response.data.url
        this.$notify.success({
          title: '成功',
          message: '上传成功'
        })
      }).catch(err => {
        console.log(err)
        this.$message.error('上传失败，请重新上传')
      })
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
    .avatar-uploader .el-upload {
    width: 145px;
    height: 145px;
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }

  .avatar-uploader .el-upload:hover {
    border-color: #20a0ff;
  }

  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 120px;
    height: 120px;
    line-height: 120px;
    text-align: center;
  }

  .avatar {
    width: 145px;
    height: 145px;
    display: block;
  }

</style>
