<!--
/**
* @author huzhiheng
* @date 2021-10-20
* @desc 邮件分组列表组件
*/
-->
<template>
  <div class="email">
    <div style="padding-bottom: 20px; height: 30px;">
      <span class="span-left">
        <h4 class="page-title">邮件分组</h4>
      </span>
      <span class="span-breadcrumb">
        <el-breadcrumb separator="/">
          <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
          <el-breadcrumb-item>配置管理</el-breadcrumb-item>
          <el-breadcrumb-item>邮件分组</el-breadcrumb-item>
        </el-breadcrumb>
      </span>
    </div>
    <el-card class="main-card">
      <h1>邮件配置</h1>
    </el-card>
  </div>
</template>

<script>

export default {
  components: {
    // 引用组件
  },
  data() {
    return {
      // 数据定义
    }
  },

  mounted() {
    // 加载前
  },

  methods: {
    // 定义方法
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* 定义当前组件使用的CSS */
</style>
