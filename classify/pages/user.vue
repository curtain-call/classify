<template>
	<view>

		<image class="background" src="../static/background.png"></image>

		<view class="search">
			<uni-search-bar bgColor="#FCF8E1" @confirm="search" v-model="searchValue" @blur="blur" @focus="focus"
				@input="input" @cancel="cancel" @clear="clear">
			</uni-search-bar>
		</view>

		<view class="card">

			<!-- <uni-card title= "请先登录" isFull="true" sub-title="地区" extra="点此修改个人信息" :thumbnail="avatar"
				@click="actionsClick()" >
				<text class="uni-body"> </text>
			</uni-card> -->

			<uni-card title="Gardenia" isFull="true" sub-title="湖北 武汉" extra="点此修改个人信息" :thumbnail="avatar"
				@click="actionsClick()">
				<text class="uni-body"> </text>
			</uni-card>
		</view>



		<view class="list_">
			<uni-list>
				<uni-list-item class="list_item" title="帮助中心" showArrow link="redirectTo" @click="onClick()" />
				<uni-list-item class="list_item" title="个人设置" showArrow link="redirectTo" @click="onClick()" />
				<uni-list-item class="list_item" title="隐私条款" showArrow link="redirectTo" @click="onClick3()" />
				<uni-list-item class="list_item" title="意见反馈" showArrow link="redirectTo" @click="onClick4()" />
			</uni-list>
		</view>

	</view>
</template>

<script>
	export default {
		data() {
			return {
				searchValue: ' ',
				avatar: "/static/maoyuna.png"


			}
		},
		onLoad() {

		},
		methods: {

			actionsClick(text) {

				// uni.showToast({
				// 	title: '登录功能正在维护中……',
				// 	icon: 'none'
				// })

				uni.navigateTo({
					url: "load/load"
				})

			},
			onClick(e) {
				console.log('执行click事件', e)
				uni.navigateTo({
					url: './file/file'
				})
			},
			onClick3(e) {
				console.log('执行click事件', e)
				uni.navigateTo({
					url: './privacy/privacy'
				})
			},
			onClick4(e) {
				console.log('执行click事件', e)
				uni.navigateTo({
					url: './bailan/bailan'
				})
				// uni.showToast({
				// 	title: '暗夜模式功能正在维护中',
				// 	icon: "none"
				// });
			},
			
			search(res) {

			},
			input(res) {
				console.log('----input:', res)
			},
			clear(res) {

			},
			blur(res) {

			},
			focus(e) {

			},
			cancel(res) {

			},

			onClickItem(e) {
				if (this.current !== e.currentIndex) {
					this.current = e.currentIndex
				}

			},
			onBackPress() {
				// #ifdef APP-PLUS
				plus.key.hideSoftKeybord();
				// #endif
			}


		}

	}
</script>
<style>
	.background {
		position: fixed;
		width: 100%;
		height: 100%;
		top: 0;
		left: 0;
		z-index: -1;
	}


	.card {
		margin-top: 330rpx;
		width: 100%
	}


	.list_ {

		width: 100%;
		margin-top: 150rpx;

	}

	.slot-box {
		/* #ifndef APP-NVUE */
		display: flex;
		/* #endif */
		flex-direction: row;
		align-items: center;
	}

	.list_item {
		height: 70px;
	}
</style>
