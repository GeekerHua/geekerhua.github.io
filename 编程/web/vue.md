

## 生命周期

![Vue 实例生命周期](assets/Vue 实例生命周期.png)

## 基本语法

缩写

### [`v-bind` 缩写](https://cn.vuejs.org/v2/guide/syntax.html#v-bind-%E7%BC%A9%E5%86%99)

```html
<!-- 完整语法 -->
<a v-bind:href="url">...</a>

<!-- 缩写 -->
<a :href="url">...</a>
```

### [`v-on` 缩写](https://cn.vuejs.org/v2/guide/syntax.html#v-on-%E7%BC%A9%E5%86%99)

```html
<!-- 完整语法 -->
<a v-on:click="doSomething">...</a>

<!-- 缩写 -->
<a @click="doSomething">...</a>
```



## vue属性

```javascript
var vm = new Vue({
  el: '#example',
  data: {
    message: 'Hello'
  },
  computed: {
    // 计算属性的 getter
    reversedMessage: function () {
      // `this` 指向 vm 实例
      return this.message.split('').reverse().join('')
    }
  },
  methods: {
      reversedMessage: function () {
        return this.message.split('').reverse().join('')
      }
  }
})
```

1. [计算属性缓存 vs 方法](https://cn.vuejs.org/v2/guide/computed.html#%E8%AE%A1%E7%AE%97%E5%B1%9E%E6%80%A7%E7%BC%93%E5%AD%98-vs-%E6%96%B9%E6%B3%95) 计算属性仅当绑定的数据变更时才会重新计算，而方法每次调用都会去计算，计算属性有缓存的作用，而方法不会缓存。
2. [计算属性 vs 侦听属性](https://cn.vuejs.org/v2/guide/computed.html#%E8%AE%A1%E7%AE%97%E5%B1%9E%E6%80%A7-vs-%E4%BE%A6%E5%90%AC%E5%B1%9E%E6%80%A7) 能使用计算属性就不使用侦听属性，避免侦听属性滥用。

### 数组的变更及检测

> 由于js的限制不能响应式更新的情况如下：

1. 当你利用索引直接设置一个项时，例如：`vm.items[indexOfItem] = newValue`
2. 当你修改数组的长度时，例如：`vm.items.length = newLength`

解决方法：

```js
// Vue.set
Vue.set(vm.items, indexOfItem, newValue)
// Array.prototype.splice
vm.items.splice(indexOfItem, 1, newValue)

vm.$set(vm.items, indexOfItem, newValue)
// 第二个问题
vm.items.splice(newLength)
```



### 对象变更及检测

> ### #### **Vue 不能检测对象属性的添加或删除**。但是，可以使用 `Vue.set(object, key, value)` 方法向嵌套对象添加响应式属性

