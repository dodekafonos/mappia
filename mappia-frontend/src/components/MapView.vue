<template>
    <l-map :zoom="zoom" :center="center" ref="mapRef" style="height: 100%">
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
    emits: ['update:mapRef'],
    mounted() {
      this.$emit('update:mapRef', this.$refs.mapRef)
    },
    components: {
      LMap,
      LTileLayer,
      LMarker,
    },
  }
  </script>
  