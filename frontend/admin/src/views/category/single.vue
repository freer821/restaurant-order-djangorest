<template>
  <div class="app-container">

    <el-card class="box-card">
      <h3>分类 -  {{ title }}</h3>
      <el-form ref="category" :rules="rules" :model="category" label-width="150px">
        <el-form-item label="产品名称" prop="name">
          <el-input v-model="category.name" />
        </el-form-item>
        <el-form-item label="商品图片">
          <el-upload
            :http-request="uploadImg"
            :show-file-list="false"
            class="avatar-uploader"
            accept=".jpg,.jpeg,.png,.gif"
          >
            <img v-if="category.content.img" :src="category.content.img" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon" />

          </el-upload>
        </el-form-item>
        <el-form-item label="是否启用">
          <el-radio-group v-model="category.isactived">
            <el-radio :label="true">是</el-radio>
            <el-radio :label="false">否</el-radio>
          </el-radio-group>
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
import { createAdminStorage } from '@/api/storage'

import { getCategoryAdmin, updateCategoryAdmin, createCategoryAdmin } from '@/api/category'
export default {
  name: 'CategoryCreateOrEdit',

  data() {
    return {
      title: '',
      category: {
        name: '',
        isactived: true,
        content: {
          img: ''
        }
      },
      origin_category: {},
      rules: {
        name: [{ required: true, message: '产品名称不能为空', trigger: 'blur' }]
      }
    }
  },
  created() {
    if (this.$route.query.id) {
      getCategoryAdmin(this.$route.query.id).then(respone => {
        this.category = respone.data
        this.title = this.category.name
        this.origin_category = Object.assign({}, this.category)
      }).catch(err => {
        console.log(err)
        this.$message.error('加载失败')
      })
    } else {
      this.title = '新建'
    }
  },
  methods: {
    submitForm() {
      this.$refs.category.validate((valid) => {
        if (valid) {
          if (!this.$route.query.id) {
            createCategoryAdmin(this.category).then(response => {
              this.$confirm('新建成功', '新建分类', {
                confirmButtonText: '返回分类列表'
              }).then(() => {
                this.$router.push('list')
              })
            }).catch(err => {
              this.$notify.error('新建失败： ' + JSON.stringify(err.msg))
            })
          } else {
            updateCategoryAdmin(this.category).then(response => {
              this.$confirm('修改成功', '修改分类', {
                confirmButtonText: '返回分类列表'
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
      this.category = this.origin_category
    },
    uploadImg(item) {
      const formData = new FormData()
      formData.append('size', item.file.size)
      formData.append('name', item.file.name)
      formData.append('file', item.file)

      createAdminStorage(formData).then(response => {
        this.category.content.img = response.data.url
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
