<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
}

body {
  margin: 0px 0px 0px;
}

html,
body {
  height: 100%;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.span-left {
  float: left;
}

.span-right {
  float: right;
}

.main-card {
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 30px;
  padding-right: 30px;
  margin-bottom: 50px;
}

.el-button--primary {
  box-shadow: 0 2px 6px 0 rgb(114 124 245 / 50%);
}

.el-button--danger {
  box-shadow: 0 2px 6px 0 rgb(250 92 124 / 50%);
}

.el-button--default {
  box-shadow: 0 2px 6px 0 rgb(114 124 245 / 50%);
}

</style>
