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

    <Toolbar>
      <RecenterButton @recenter="recenterMap" />
      <NewEventButton @click="enableNewEventMode" />
    </Toolbar>

    <NewEventDrawer
      v-model:visible="isDrawerVisible"
      :location="selectedLocation"
    />


  </div>
</template>

<script>
import MapView from '@/components/MapView.vue'
import RecenterButton from '@/components/RecenterButton.vue'
import Loading from '@/components/Loading.vue'
import NewEventButton from '@/components/NewEventButton.vue'
import Toolbar from '@/components/Toolbar.vue'
import NewEventDrawer from '@/components/NewEventDrawer.vue'

export default {
  components: {
    MapView,
    RecenterButton,
    Loading,
    NewEventButton,
    Toolbar,
    NewEventDrawer,
  },
  data() {
    return {
      isDrawerVisible: false,
      zoom: 16,
      center: null,
      selectedLocation: null,
      isCreatingEvent: false,
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
    getMap() {
      return this.$refs.mapComponent?.$refs.mapRef?.leafletObject || null
    },
    enableNewEventMode() {
      this.isCreatingEvent = true
      const map = this.getMap()
      if (map) {
        map.getContainer().style.cursor = 'pointer'
      }
    },
    handleMapClick(latlng) {
      if (this.isCreatingEvent) {
        console.log('Coordenadas do novo evento:', latlng)
        this.isCreatingEvent = false
        this.selectedLocation = latlng
        this.isDrawerVisible = true 

        const map = this.getMap()
        if (map) {
          map.getContainer().style.cursor = ''
        }
      }
    },
    closeDrawer() {
      this.selectedLocation = null
    },
  },
}
</script>

<style scoped>
.map-container {
  width: 100%;
  height: 100%;
  position: relative;
  z-index: 10;
}
</style>
