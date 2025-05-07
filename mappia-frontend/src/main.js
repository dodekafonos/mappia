import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'

import '../main.css'
import 'leaflet/dist/leaflet.css'
import 'primeicons/primeicons.css'

import PrimeVue from 'primevue/config'
import Drawer from 'primevue/drawer'
import Aura from '@primeuix/themes/aura'

import L from 'leaflet'

// Corrige ícones padrão do Leaflet
delete L.Icon.Default.prototype._getIconUrl
L.Icon.Default.mergeOptions({
  iconRetinaUrl: new URL('leaflet/dist/images/marker-icon-2x.png', import.meta.url).href,
  iconUrl: new URL('leaflet/dist/images/marker-icon.png', import.meta.url).href,
  shadowUrl: new URL('leaflet/dist/images/marker-shadow.png', import.meta.url).href,
})

// Define rotas
const routes = [
  { path: '/', component: () => import('./view/Home.vue') },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

// Cria a instância do app antes de montar
const app = createApp(App)

app.use(router)
app.use(PrimeVue, {
  theme: {
    preset: Aura
  }
})

// Registra globalmente o componente Drawer
app.component('Drawer', Drawer)

// Monta o app
app.mount('#app')
