

<script>
	

	
	export default {
		
		onLaunch: function() {
			uni.navigateTo({
				url:"pages/picture"
			})
			console.log('App Launch')
			uni.onTabBarMidButtonTap(()=>{
			uni.chooseImage({
			count: 1,
			sourceType: ['camera'],
			success: function (res) {
				uni.saveImageToPhotosAlbum({
					filePath: res.tempFilePaths[0],
					success: function () {
						console.log('save success');
					}
				});
			}
		})
			}
			
    )
		},
		
		
		
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		}
		
		
		
		}
		
	
</script>

<style>
	
	
	

	.background{
		position: fixed;
		width: 100%;
		height: 100%;
		z-index: -1;
		top: 0;
		bottom:0;
	}
	
	.search-result {
				padding-top: 10px;
				padding-bottom: 20px;
				text-align: center;
			}
		
			.search-result-text {
				text-align: center;
				font-size: 14px;
				color:#666;
			}
		
			.example-body {
				/* #ifndef APP-NVUE */
				
				display: block;
				/* #endif */
				padding: 0px;
			}
		
			.uni-mt-10 {
				margin-top: 10px;
			}
			
			.search{
				position:absolute;
				top:90rpx;
				right:0rpx;
				display: block;
				width: 100%;
			}
	/*每个页面公共css */
	
	.uni-margin-wrap {
			width: 690rpx;
			width: 100%;
		}
		.swiper {
			height: 300rpx;
		}
		.swiper-item {
			display: block;
			height: 300rpx;
			line-height: 300rpx;
			text-align: center;
		}
		.swiper-list {
			margin-top: 40rpx;
			margin-bottom: 0;
		}
		.uni-common-mt {
			margin-top: 60rpx;
			position: relative;
		}
		.info {
			position: absolute;
			right: 20rpx;
		}
		.uni-padding-wrap {
			width: 550rpx;
			padding: 0 100rpx;
		}
</style>
 