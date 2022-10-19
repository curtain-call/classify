<template>
	<view>
		<image class="background" src="../static/background.png"></image>
		<!-- <view class="search-bar">
			<input  type="text" v-module="val" placeholder="请输入您要搜索的内容 " confirm-type="search"
				@confirm="doSearch">
		</view> -->
		<view class="sousuo" :style="{'margin-left': isShowFocus?'5%':'','width':width}">
			<view class="sousuo_ico"><text class="iconfont icon-sousuo"></text></view>
			<view class="sousuo_input"><input type="text" @focus="onFocusInput" @blur="onBlurInput"
					placeholder-class="sousuo_placeholder" v-model="inpuval" :placeholder="placeholder" /></view>
			<view class="sousuo_cances" @click="inputCances" v-if="isShowFocus">取消</view>
		</view>


		<view>
			<view class="uni-swiper1">
				<swiper circular :indicator-dots="true" :autoplay="true" :interval="5000" :duration="500"
					:style="{height: listHeight}">
					<swiper-item>
						<view class="swiper_item" mode="">
							<image :src="this.list[1].path" mode=""></image>
							<!-- <image src="../static/picture1.png" @load="fixSwiperHeight"></image> -->
						</view>
					</swiper-item>
					<swiper-item>
						<view class="swiper_item" mode="">
							<image :src="this.list[2].path" mode=""></image>
							<!-- <image src="../static/picture2.png" @load="fixSwiperHeight"></image> -->
						</view>
					</swiper-item>
					<swiper-item>
						<view class="swiper_item" mode="">
							<image :src="this.list[3].path" mode=""></image>
							<!-- <image src="../static/picture3.png" @load="fixSwiperHeight"></image> -->
						</view>
					</swiper-item>
					<swiper-item>
						<view class="swiper_item" mode="">
							<image :src="this.list[4].path" mode=""></image>
							<!-- <image src="../static/picture4.png" @load="fixSwiperHeight"></image> -->
						</view>
					</swiper-item>
				</swiper>
			</view>
		</view>


		<view class="swip">
			<swiper :indicator-dots="true" :autoplay="true" :interval="3000" :duration="1000">
				<swiper-item class="swiper-item">
					<!-- <image :src="this.list[0].path" mode=""></image> -->
					<image src="../static/picture1.png" @load="fixSwiperHeight"></image>
				</swiper-item>

				<swiper-item class="swiper-item">
					<!-- <image :src="this.list[1].path" mode=""></image> -->
					<image src="../static/picture2.png" @load="fixSwiperHeight"></image>
				</swiper-item>
				<swiper-item class="swiper-item">
					<!-- <image :src="this.list[3].path" mode=""></image> -->
					<image src="../static/picture3.png" @load="fixSwiperHeight"></image>
				</swiper-item>
				<swiper-item class="swiper-item">
					<!-- <image :src="this.list[4].path" mode=""></image> -->
					<image src="../static/picture4.png" @load="fixSwiperHeight"></image>
				</swiper-item>
			</swiper>

		</view>

		<!-- <swiper :indicator-dots="true" :autoplay="true" :interval="3000" :duration="1000">
		<swiper-item>
			<view class="swiper-item1">
				<image src="../static/picture1.png" mode=""></image>
			</view>
		</swiper-item>
		<swiper-item>
			<view class="swiper-item1">
				<image src="../static/picture2.png" mode=""></image>
			</view>
		</swiper-item>
	</swiper>
 -->




	</view>
</template>

<script>
	const FilesModule = uni.requireNativePlugin('lu-FilesModule');

	export default {

		data() {
			return {
				searchValue: ' ',
				list: [],
				// list: [{path:"图片绝对路径", pkg: "图片的创作者包名", date: "创建时间（时间戳）}...]
				indicatorDots: true,
				autoplay: true,
				interval: 2000,
				duration: 500,

				//搜索框
				isShowFocus: false,
				inpuval: '',
				width: "90%"

			}

		},

		onLoad() {
			this.getImageFileList()
			console.log('fetch the temporary path!')
		},
		methods: {

			onFocusInput: function(event) {
				//console.log('输入框聚焦时触发:',event)
				// this.inputValue = event.target.value
				this.isShowFocus = true;
				this.width = "80%";
				this.$emit("focus")
			},
			onBlurInput: function(event) {
				//console.log("输入框失去焦点时触发:",event); 
				this.$emit("blur")

			},
			inputCances: function() {
				this.isShowFocus = false;
				this.inpuval = '';
				this.width = "90%"
				this.$emit("cancel");
			},
			//上面三个是搜索框的

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

			//读取照片列表
			
			getImageFileList() {
									FilesModule.getImageFileList((res) => {
										//res格式  {code: 200, msg: "提示内容", list: [{path:"图片绝对路径", pkg: "图片的创作者包名", date: "创建时间（时间戳）"}, ...]}  开发者可自行打印
										if (res.code === 200) {
											for(var i=0;i<res.list.length;i++){
											this.list.push(res.list[i])							
											}
											console.log('success!')
											console.log(this.list[0].path)	
											// 同步更新data
										} else {
											//获取文件列表错误
											uni.showToast({
												title: '错误：' + res.msg,
												icon: 'none'
											});
										}
									});
								},

			//读取视频文件列表
			getVideoFileList() {
				FilesModule.getVideoFileList((res) => {
					//res格式  {code: 200, msg: "提示内容", list: [{path:"图片绝对路径", pkg: "图片的创作者包名", date: "创建时间（时间戳）"}, ...]}  开发者可自行打印
					if (res.code === 200) {
						console.log(res);
						this.msg = JSON.stringify(res);
					} else {
						//获取文件列表错误
						uni.showToast({
							title: '错误：' + res.msg,
							icon: 'none'
						});
					}
				});
			},

			intervalChange(e) {
				this.interval = e.target.value
			},
			durationChange(e) {
				this.duration = e.target.value
			},

			//更改swiper高度
			fixSwiperHeight() {
				let _this = this
				let proImg = this.$refs.proImg;
				this.listHeight = proImg[0].height + 30 + 'px';
			},

		}


	}
</script>

<style>
	swiper {
		width: 100%;
		height: 600rpx;
	}

	.search-bar {
		margin-top: 50px;
		background-color: #FCF8E1;
		height: 35px;



	}

	.background {
		position: fixed;
		width: 100%;
		height: 100%;
		top: 0;
		left: 0;
		z-index: -1;
	}


	/* .uni-common-mt {
		margin-top: 40px;
	}
 */
	.container {

		padding: 20px;
		font-size: 14px;
		line-height: 24px;
	}

	.randOne {}

	/*图片的swiper*/
	.swip {
		margin-top: 50px;
		margin-left: auto;
		margin-right: auto;
		align-items: center;
	}

	.swip image {
		height: 400px;
	}

	/*相册的swiper*/
	.uni-swiper1 {
		margin-top: 0px;
		margin-left: auto;
		justify-content: center;
		align-items: center;
		display: flex;
	}

	.uni-swiper1 image {
		width: 100%;
		height: 350px;
	}

	/* .uni-swiper {
		margin-top: 500px;
	} */

	/* .swiper-box {
		height: 200px;
	}
 */
	/*图片的swiper item*/
	.swiper-item {
		/* #ifndef APP-NVUE */
		display: flex;
		/* #endif */
		flex-direction: column;
		justify-content: center;
		align-items: center;
		height: 200px;
		color: #fff;
	}

	/* .swiper-item image{
		width:100%;
	} */

	/*相册的swiper item*/
	.swiper_item {
		/* #ifndef APP-NVUE */
		display: flex;
		/* #endif */
		flex-direction: column;
		justify-content: center;
		align-items: center;
		height: 400px;
		color: #fff;
	}




	/* #ifndef APP-NVUE */
	::v-deep .image img {
		-webkit-user-drag: none;
		-khtml-user-drag: none;
		-moz-user-drag: none;
		-o-user-drag: none;
		user-drag: none;
	}

	/* #endif */

	@media screen and (min-width: 500px) {
		.uni-swiper-dot-box {
			width: 400px;
			margin: 0 auto;
			margin-top: 8px;
			height: 500px;
		}

		.image {
			width: 100%;

		}
	}



	.example-body {
		/* #ifndef APP-NVUE */
		display: flex;
		/* #endif */
		flex-direction: row;
		padding: 20rpx;
	}

	/*底下全部是搜索框*/
	.sousuo {
		display: flex;
		align-content: center;
		align-items: center;
		background-color: #FCF8E1;
		padding: 5px 0;
		margin-left: 5%;
		margin-top: 50px;
		margin-bottom: 0px;
		border-radius: 5px;
	}

	.sousuo_ico {
		width: 10%;
		text-align: center;
	}

	.sousuo_input {
		width: 96%;
		margin-top: 5px;
		font-size: 10px;
		letter-spacing: 1px;

	}

	.sousuo_placeholder {
		font-size: 10px;
		color: #7E7E7E;
	}

	.sousuo_cances {
		position: absolute;
		width: 90%;
		text-align: right;
		font-size: 14px;
		color: #000000;

	}
</style>
