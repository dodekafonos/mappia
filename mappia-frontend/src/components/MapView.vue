<template>
  <l-map
    :zoom="zoom"
    :center="center"
    ref="mapRef"
    style="height: 100%"
    @click="onMapClick"
  >
    <l-tile-layer
      url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    />
  </l-map>
</template>

<script>
import { LMap, LTileLayer } from '@vue-leaflet/vue-leaflet'

export default {
  props: ['center', 'zoom'],
  emits: ['update:mapRef', 'map-click'],
  components: {
    LMap,
    LTileLayer,
  },
  mounted() {
    this.$emit('update:mapRef', this.$refs.mapRef)
  },
  methods: {
    onMapClick(event) {
      this.$emit('map-click', event.latlng)
    },
  },
}
</script>
