<template>
  <div class="map-container" style="height: 100vh;">
    <MapView v-if="center" :center="center" :zoom="zoom" ref="mapComponent" />
    <Loading v-else />

    <RecenterButton @recenter="recenterMap" />
  </div>
</template>

<script>
import MapView from '../components/MapView.vue'
import RecenterButton from '../components/RecenterButton.vue'
import Loading from '../components/Loading.vue'

export default {
  components: {
    MapView,
    RecenterButton,
    Loading,
  },
  data() {
    return {
      zoom: 16,
      center: null,
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

            const map = this.$refs.mapComponent?.$refs.mapRef?.leafletObject
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
