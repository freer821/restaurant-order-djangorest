<template>
  <div class="app-container">
    <el-steps :active="active" finish-status="success" align-center>
      <el-step title="产品信息" />
      <el-step title="包裹信息" />
      <el-step title="收件人信息" />
      <el-step title="物流信息" />
    </el-steps>

    <el-form ref="chuku" :rules="rules" :model="chuku" label-width="150px">

      <el-card v-show="showStatus[0]" class="box-card">
        <h3>产品信息</h3>
        <el-tooltip class="item" effect="dark" content="例如： 维修品， 耗材等" placement="bottom">
          <el-form-item label="物品类型" prop="type">
            <el-input v-model="chuku.type" />
          </el-form-item>
        </el-tooltip>
        <el-tooltip class="item" effect="dark" content="例如： 产品型号" placement="bottom">
          <el-form-item label="产品名字" prop="product_name">
            <el-input v-model="chuku.product_name" />
          </el-form-item>
        </el-tooltip>

        <el-form-item label="SN号" prop="sn_code">
          <el-input v-model="chuku.sn_code" />
        </el-form-item>
        <el-form-item label="平台" prop="platform">
          <el-input v-model="chuku.platform" />
        </el-form-item>
        <el-form-item label="负责人" prop="contact">
          <el-input v-model="chuku.contact" />
        </el-form-item>
        <el-form-item style="text-align: center">
          <el-button type="primary" size="medium" @click="nextStep">下一步，包裹信息</el-button>
        </el-form-item>
      </el-card>
      <el-card v-show="showStatus[1]" class="box-card">
        <h3>包裹信息</h3>
        <el-tooltip class="item" effect="dark" content="例如： 主机-良品，配件等" placement="bottom">
          <el-form-item label="内物类型" prop="pack_content">
            <el-input v-model="chuku.pack_content" />
          </el-form-item>
        </el-tooltip>

        <el-form-item label="打包类型" prop="pack_type">
          <el-radio-group v-model="chuku.pack_type">
            <el-radio label="carton">纸箱</el-radio>
            <el-radio label="pallet">托盘</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item
          label="内物数量"
          prop="num"
        >
          <el-input v-model="chuku.num" type="number" placeholder="0" />
        </el-form-item>
        <el-form-item label="毛重KG" prop="weight">
          <el-input v-model="chuku.weight" />
        </el-form-item>

        <el-row :gutter="20">
          <el-col :span="8">
            <el-form-item label="长 (cm)">
              <el-input v-model="chuku.long" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="宽 (cm)">
              <el-input v-model="chuku.width" />
            </el-form-item>
          </el-col>
          <el-col :span="8">
            <el-form-item label="高 (cm)">
              <el-input v-model="chuku.height" />
            </el-form-item>
          </el-col>
        </el-row>

        <el-form-item style="text-align: center">
          <el-button size="medium" @click="prevStep">上一步，产品信息</el-button>
          <el-button type="primary" size="medium" @click="nextStep">下一步，收件人信息</el-button>
        </el-form-item>
      </el-card>
      <el-card v-show="showStatus[2]" class="box-card">
        <h3>收件人信息</h3>
        <el-form-item label="收件人">
          <el-input v-model="chuku.reciever.name" />
        </el-form-item>
        <el-form-item label="公司名称/包裹站编码">
          <el-input v-model="chuku.reciever.company" />
        </el-form-item>
        <el-form-item label="街道">
          <el-input v-model="chuku.reciever.addr" />
        </el-form-item>
        <el-form-item label="门牌号">
          <el-input v-model="chuku.reciever.housenr" />
        </el-form-item>
        <el-form-item label="城市">
          <el-input v-model="chuku.reciever.city" />
        </el-form-item>
        <el-form-item label="州/省">
          <el-input v-model="chuku.reciever.provice" />
        </el-form-item>
        <el-form-item label="邮编">
          <el-input v-model="chuku.reciever.postcode" />
        </el-form-item>
        <el-form-item label="国家">
          <el-input v-model="chuku.reciever.country" />
        </el-form-item>
        <el-form-item label="备注">
          <el-input v-model="chuku.reciever.extra" type="textarea" :rows="2" placeholder="请输入内容" />
        </el-form-item>
        <el-form-item style="text-align: center">
          <el-button size="medium" @click="prevStep">上一步，包裹信息</el-button>
          <el-button type="primary" size="medium" @click="nextStep">下一步，物流信息</el-button>
        </el-form-item>
      </el-card>
      <el-card v-show="showStatus[3]" class="box-card">
        <h3>物流信息</h3>
        <el-form-item label="物流公司" prop="logistic_company">
          <el-input v-model="chuku.logistic_company" />
        </el-form-item>
        <el-form-item label="物流单号" prop="logistic_code">
          <el-input v-model="chuku.logistic_code" />
        </el-form-item>
        <el-tooltip class="item" effect="dark" content="例如： 快递-送件，FBA仓-送件等" placement="bottom">
          <el-form-item label="物流类型" prop="logistic_type">
            <el-input v-model="chuku.logistic_type" />
          </el-form-item>
        </el-tooltip>

        <el-form-item label="FBA单号" prop="fba_code">
          <el-input v-model="chuku.fba_code" />
        </el-form-item>

        <el-form-item label="备注">
          <el-input v-model="chuku.comment" type="textarea" :rows="2" placeholder="请输入内容" />
        </el-form-item>
        <el-form-item style="text-align: center">
          <el-button size="medium" @click="prevStep">上一步，收件人信息</el-button>
        </el-form-item>
      </el-card>
    </el-form>

    <div class="op-container">
      <el-button @click="resetForm">重置</el-button>
      <el-button type="primary" @click="submitForm">提交</el-button>
    </div>
  </div>
</template>

<script>
import { updateUserChuku, getUserChuku } from '@/api/chuku'
export default {
  name: 'ChukuEdit',

  data() {
    return {
      active: 0,
      showStatus: [true, false, false, false],
      chuku: {
        product_name: '',
        num: undefined,
        contact: '',
        platform: '',
        type: '',
        pack_type: '',
        pack_content: '',
        sn_code: '',
        reciever: {
          name: '',
          company: '',
          tel: '',
          addr: '',
          housenr: '',
          city: '',
          provice: '',
          postcode: '',
          country: '',
          extra: ''
        },
        logistic_type: '',
        weight: undefined,
        long: undefined,
        width: undefined,
        height: undefined,
        fba_code: '',
        logistic_code: '',
        logistic_company: '',
        comment: ''
      },
      rules: {
        product_name: [{ required: true, message: '产品名称不能为空', trigger: 'blur' }],
        pack_content: [{ required: true, message: '内物类型不能为空', trigger: 'blur' }],
        num: [
          { required: true, message: '不能为空或非数字', trigger: 'blur' }
        ]
      },
      origin_chuku: {}
    }
  },
  created() {
    getUserChuku(this.$route.query.id).then(respone => {
      this.chuku = respone.data
      this.origin_chuku = Object.assign({}, this.chuku)
    }).catch(err => {
      console.log(err)
      this.$message.error('加载失败')
    })
  },
  methods: {
    hideAll() {
      for (let i = 0; i < this.showStatus.length; i++) {
        this.showStatus[i] = false
      }
    },
    prevStep() {
      if (this.active > 0 && this.active < this.showStatus.length) {
        this.active--
        this.hideAll()
        this.showStatus[this.active] = true
      }
    },
    nextStep() {
      if (this.active < this.showStatus.length - 1) {
        this.active++
        this.hideAll()
        this.showStatus[this.active] = true
      }
    },
    submitForm() {
      this.$refs.chuku.validate((valid) => {
        if (valid) {
          delete this.chuku.createdtime
          updateUserChuku(this.chuku).then(response => {
            this.$message.success('修改成功！')
            this.$router.push({ path: '/chuku/list' })
          }).catch(err => {
            this.$message.error(JSON.stringify(err.msg))
          })
        } else {
          this.$message.error('输入有误，请检查！')
          return false
        }
      })
    },
    resetForm() {
      this.chuku = Object.assign({}, this.origin_chuku)
    }
  }
}
</script>

<style scoped>
  .el-card {
    margin: 50px;
  }

</style>
