import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MaterialDetail from '../views/MaterialDetail.vue'
import MaterialAdd from '../views/MaterialAdd.vue'
import MaterialEdit from '../components/MaterialEdit.vue'
const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/MaterialAdd',
    name: 'MaterialAdd',
    component: MaterialAdd
  },
  {
    path: '/materials/:id',
    name: 'MaterialDetail',
    component: MaterialDetail,
    props: true
  },
  {
    path: '/materials/:id/edit',
    name: 'MaterialEdit',
    component: MaterialEdit,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router