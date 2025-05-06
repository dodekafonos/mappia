<template>
  <l-map
    :zoom="zoom"
    :center="center"
    ref="mapRef"
    style="height: 100%"
    @ready="onMapReady"
  >
    <l-tile-layer
      url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    />
    <l-marker :lat-lng="center" />
  </l-map>
</template>

<script>
import { LMap, LTileLayer, LMarker } from '@vue-leaflet/vue-leaflet'

export default {
  props: ['center', 'zoom'],
  emits: ['map-click', 'update:mapRef'],
  components: {
    LMap,
    LTileLayer,
    LMarker,
  },
  methods: {
    onMapReady() {
      const map = this.$refs.mapRef.leafletObject
      this.$emit('update:mapRef', this.$refs.mapRef)

      // Adiciona o listener de clique no mapa
      map.on('click', e => {
        this.$emit('map-click', e.latlng)
      })
    },
  },
}
</script>
