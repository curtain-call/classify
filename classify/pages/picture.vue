<template>
	<view class="container">
		<image class="background" src="../static/background.png"></image>

		<view class="header">
			<view class="icon1">
				<uni-icons size="30" type="plus"></uni-icons>
				<span style="margin-left: 30rpx;"></span>
				<uni-icons size="30" type="more"></uni-icons>
			</view>
			<text style="width: 100%;">相册</text>

		</view>

		<view class="albumsearch">
			<uni-search-bar bgColor="#FCF8E1" @confirm="search" v-model="searchValue" @blur="blur" @focus="focus"
				@input="input" @cancel="cancel" @clear="clear">试试搜索“猫猫”“狗勾”
			</uni-search-bar>
		</view>

		<view class="text">
			<text style="vertical-align: middle;"> 分类</text>
		</view>

		<view class="album">
			<image class="img" :src="items[0].uri[0]" v-if="albumappear.index1" @click="naviAlbum()"></image>
			<image class="img" :src="items[1].uri[0]" v-if="albumappear.index2" @click=""></image>
			<image class="add" src="../static/Plus5.png" @click="chooseImage()"></image>
		</view>

		<view class="text_">
			<text> 时间线</text>
		</view>
		<view class="timeline">
			<image :src="list[index].uri" class="line" v-if="albumappear.index1" v-for="(item,index) in list"></image>
		</view>


	</view>
</template>


<script>
	const FilesModule = uni.requireNativePlugin('lu-FilesModule');
	export default {
		data() {
			return {
				searchValue: ' ',
				list: [],
				// list:[{"name": "","uri": ""}...]
				id: [],
				i: 0,
				showcase: [],
				// showcase:[{"id": " " , "label": " "}...]	通过showcase进行索引，显示图片在前端页面
				// showcase的id和id[]是一一对应的，也和list的索引是一致的
				items: [{
						label: "Cat",
						uri: []
					},
					{
						label: "Dog",
						uri: []
					},
				],
				albumappear: {
					index1: false,
					index2: false,
				},

			}
		},
		onLoad() {

		},
		methods: {
			search(res) {},
			input(res) {
				console.log('----input:', res)
			},
			clear(res) {},
			blur(res) {},
			focus(e) {},
			cancel(res) {},
			onClickItem(e) {
				if (this.current !== e.currentIndex) {
					this.current = e.currentIndex
				}
			},
			onBackPress() {
				// #ifdef APP-PLUS
				plus.key.hideSoftKeybord();
				// #endif
			},

			//上面全部都是搜索框的东西

			checkAuth() {
				FilesModule.checkAuth(res => {
					console.log(res);
					if (res.code === 200) {
						//有读取文件权限
						uni.showToast({
							title: '已开启读取文件权限',
							icon: 'none'
						});
					} else if (res.code === 400) {
						//没有读取文件权限
						uni.showToast({
							title: '未开启读取文件权限',
							icon: 'none'
						});
					} else {
						//code === 4000
						uni.showToast({
							title: '权限被永久拒绝',
							icon: 'none'
						});
						//可以引导用户打开app权限目录 手动授权
					}
				});
			},

			chooseImage() {
				FilesModule.checkAuth()
				uni.chooseImage({
					success: (chosen) => {
						for (var j = 0; j < chosen.tempFilePaths.length; j++) {
							var file = {
								name: (this.i + j).toString() + '.jpg',
								uri: chosen.tempFilePaths[j]
							}
							this.list.push(file)
							this.id[this.i + j] = this.i + j
							// list:[{"name": "","uri": ""}]
						}
						this.i += chosen.tempFilePaths.length
						console.log(this.i)
						console.log(this.list)
						uni.uploadFile({
							url: 'http://192.168.43.98:8080/',
							files: this.list,
							name: 'album',
							formData: {
								'id': this.id
							},
							success: (res) => {
								this.showcase = JSON.parse(res.data)
								var uricat = []
								var uridog = []
								for (var i = 0; i < this.showcase.length; i++) {
									switch (this.showcase[i].label) {
										case "Cat":
											uricat.push(this.list[this.showcase[i].id].uri)
											break;
										case "Dog":
											uridog.push(this.list[this.showcase[i].id].uri)
											break;
										default:
											break;
									}
								}
								this.$set(this.items[0], "uri", uricat)
								this.$set(this.items[1], "uri", uridog)
								console.log(this.items)
								this.$set(this.albumappear, "index1", true)
								this.$set(this.albumappear, "index2", true)
							}
						})
						// 这儿

					}
				})
			},

			//读取照片列表
			getImageFileList() {
				FilesModule.getImageFileList((res) => {
					//res格式  {code: 200, msg: "提示内容", list: [{path:"图片绝对路径", pkg: "图片的创作者包名", date: "创建时间（时间戳）"}, ...]}  开发者可自行打印
					if (res.code === 200) {
						for (var i = 0; i < res.list.length; i++) {
							this.list.push(res.list[i].path)
							this.id[i] = i
						}
						console.log('success!')
						console.log(this.list[0])
						// 同步更新data

						uni.uploadFile({
							url: 'http://192.168.43.98:8080/',
							files: this.list,
							name: 'album',
							formData: {
								id: this.id
							},
						})
						console.log('success!')

					} else {
						//获取文件列表错误
						uni.showToast({
							title: '错误：' + res.msg,
							icon: 'none'
						});
					}
				})

			},
			
			naviAlbum(){
				uni.navigateTo({
					url:'album/album',
					events:{},
					success:function(res){
					
					}
				})
			}
		},

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

	.container {
		display: flex;
		flex-direction: row;
		justify-content: flex-start;
		flex-wrap: wrap;
		align-content: flex-start;
		align-items: center;
	}

	.choosingbox {

		width: 100%;
		height: 150rpx;
		align-items: center;
		align-content: stretch;
	}


	.header {
		margin-top: 100rpx;
		/* 空出通知栏 */
		font-size: 70rpx;
		font-style: normal;
		margin-left: 40rpx;
	}

	.albumsearch {
		margin-top: 30rpx;
		width: 100%;
	}

	.text {
		font-size: 60rpx;
		font-style: normal;
		/* margin-top: 50rpx; */
		font-weight: 500;
		margin-left: 30rpx;
		width: 100%;
		height: 150rpx;
	}

	.img {
		width: 200rpx;
		height: 200rpx;
		margin-left: 20rpx;
	}

	.add {
		width: 200rpx;
		height: 200rpx;
		order: 1;
	}

	.text_ {
		font-size: 60rpx;
		font-style: normal;
		font-weight: 500;
		margin-left: 30rpx;
		width: 100%;
		height: 150rpx;
	}

	.album {
		width: 100%;
		height: 300rpx;
	}

	.line {
		align-self: center;
		margin-left: 50rpx;
		margin-bottom: 50rpx;
	}

	.icon1 {
		margin-left: 500rpx;
		align-self: flex-start;
	}
	.icon2 {
		align-self: flex-start;
	}
</style>
