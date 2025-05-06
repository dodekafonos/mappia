<template>
  <div class="map-container" style="height: 100vh;">
    <MapView
      v-if="center"
      :center="center"
      :zoom="zoom"
      ref="mapComponent"
      @map-click="handleMapClick"
    />
    <Loading v-else />

    <RecenterButton @recenter="recenterMap" />

    <!-- Novo botão flutuante -->
    <NewEventButton
      v-if="newEventPosition"
      :position="newEventPosition"
      @click="openEventDrawer"
    />
  </div>
</template>

<script>
import MapView from '../components/MapView.vue'
import RecenterButton from '../components/RecenterButton.vue'
import NewEventButton from '../components/NewEventButton.vue'
import Loading from '../components/Loading.vue'

export default {
  components: {
    MapView,
    RecenterButton,
    NewEventButton,
    Loading,
  },
  data() {
    return {
      zoom: 16,
      center: null,
      newEventPosition: null,
    }
  },
  mounted() {
    this.recenterMap()
  },
  methods: {
    recenterMap() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          position => {
            const newCenter = [
              position.coords.latitude,
              position.coords.longitude,
            ]
            this.center = newCenter

            const map = this.getMap()
            if (map) {
              map.setView(newCenter, this.zoom)
            }
          },
          error => {
            console.error('Erro ao obter localização:', error)
          }
        )
      }
    },
    handleMapClick(latlng) {
      const map = this.getMap()
      if (map) {
        const point = map.latLngToContainerPoint(latlng)
        this.newEventPosition = {
          x: point.x,
          y: point.y,
        }
      }
    },
    getMap() {
      return this.$refs.mapComponent?.$refs.mapRef?.leafletObject || null
    },
    openEventDrawer() {
      console.log('Abrir formulário de criação de evento...')
      // Aqui abriremos a gaveta futuramente
    },
  },
}
</script>

<style scoped>
.map-container {
  width: 100%;
  height: 100%;
  position: relative;
}
</style>
