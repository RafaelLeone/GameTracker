import DefaultLayout from "@/layouts/default/DefaultLayout.vue"
import PlaylistAddView from "@/views/games/PlaylistAddView"
import GameRowView from "@/views/games/GameRowView.vue"

export default [
  {
    path: "/playlist",
    component: DefaultLayout,
    children: [
      {
        path: "add",
        name: "addPlaylist",
        component: PlaylistAddView,
      },
    ],
  },
  {
    path: "/games",
    component: DefaultLayout,
    children: [
      {
        path: "playing",
        name: "playingGames",
        component: GameRowView,
      },
    ],
  }
]