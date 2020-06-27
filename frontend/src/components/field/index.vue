<template>
  <div class="md_field" :class="{md_field_hasIcon: !!icon, md_field_isError: isError}">
    <van-icon v-if="icon" :name="icon" class="md_feld_icon" />
    <div class="md_field_control">
      <input
        :type="type"
        v-bind="$attrs"
        :value="value"
        v-on="listeners"
      >
    </div>
    <div>
      <slot name="rightIcon">
        <van-icon v-show="value" :name="rightIcon" @click="rightClick" />
      </slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MdField',

  props: {
    value: {},
    type: {
      type: String,
      default: 'text'
    },
    rightIcon: String,
    icon: String,
    isError: Boolean
  },
  computed: {
    listeners() {
      return {
        ...this.$listeners,
        input: this.onInput
      }
    }
  },

  methods: {
    onInput(event) {
      this.$emit('input', event.target.value)
    },
    rightClick(event) {
      this.$emit('right-click', event)
    }
  }
}
</script>

<style lang="scss" scoped>
.md_field {
  position: relative;
  display: table;
  box-sizing: border-box;
  width: 100%;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 10px;
  background-color: #fff;
  border: 1px solid;
  border-radius: 5px;
   > div {
    display: table-cell;
  }
   > .md_field_control {
    box-sizing: border-box;
    padding-right: 10px;
    input {
      width: 100%;
      font-size: 14px;
      line-height: 14px;
      border: 0;
    }
  }

  .md_feld_icon {
    position: absolute;
    top: 50%;
    left: 10px;
    transform: translate(0, -50%);
  }
}

.md_field_hasIcon {
  padding-left: 40px;
}

.md_field_isError {
  background-color: #fcf5f5;
  border: 1px solid;
  input {
    background-color: #fcf5f5;
  }
  input:-webkit-autofill {
    -webkit-box-shadow: 0 0 0 1000px #fcf5f5 inset !important;
  }
}
</style>
