<!--
/**
* @author huzhiheng
* @date 2021-10-20
* @desc 环境列表组件
*/
-->
<template>
  <div class="env">
    <div style="padding-bottom: 20px; height: 30px;">
      <span class="span-left">
        <h4 class="page-title">环境管理</h4>
      </span>
      <span class="span-breadcrumb">
        <el-breadcrumb separator="/">
          <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
          <el-breadcrumb-item>配置管理</el-breadcrumb-item>
          <el-breadcrumb-item>环境管理</el-breadcrumb-item>
        </el-breadcrumb>
      </span>
    </div>
    <el-card class="main-card">
      <h1>环境管理</h1>
    </el-card>
  </div>
</template>

<script>

export default {
  name: 'env',
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
