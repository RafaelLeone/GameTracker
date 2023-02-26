<template>
    <v-navigation-drawer
      expand-on-hover
      rail
    >
      <v-list>
        <v-list-item
          prepend-avatar="https://upload.wikimedia.org/wikipedia/commons/f/f4/Video-Game-Controller-Icon.svg"
          title="GameTracker"
          subtitle="It's a secret to everybody"
        ></v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list density="compact" nav>
        <v-list-item
          prepend-icon="mdi-home"
          title="Início"
          :to="{ name:'base-home' }"
        >
        </v-list-item>
        <game-form />
        <v-list-item
          :prepend-icon="theme === 'light' ? 'mdi-weather-sunny' : 'mdi-weather-night'"
          title="Change theme"
          @click.stop="themeClick">
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
</template>

<script>
import GameForm from "@/components/GameForm.vue"

export default {
  components: {
    GameForm
  },
  props: {
    title: {
      type: String,
      required: false,
      default: "SpotBye",
    },
    theme: {
      type: String,
      required: true,
      default: "dark",
    },
  },
  emits: ["themeClick"],
  data: () => {
    return {}
  },
  methods: {
    themeClick() {
      this.$emit("themeClick")
    },
  },
}
</script>
