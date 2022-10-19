<template>
	<view >
		<image class="background" src="../static/cloud_background.png"></image>
		
		 <view class="search">
				<uni-search-bar bgColor="#FCF8E1" @confirm="search" v-model="searchValue" @blur="blur" @focus="focus" @input="input"
					@cancel="cancel" @clear="clear"c>
				</uni-search-bar>
				
				
				<image class="storage" src="../static/storage.png"></image>
				
				<view class="选项">
					
				    <view class="uni-padding-wrap uni-common-mt">
								<uni-segmented-control :current="current" :values="items" :style-type="styleType"
									:active-color="activeColor" @clickItem="onClickItem" />
							</view>
							 </view>
							
			     
				 <image class="list" src="../static/list_file.png"></image>
				</view> 
		<view class="content"></view>
		<view class="text-area">
		</view>
	</view>
</template>

<script>
	export default {
			data() {
				return {
					searchValue: ' ',
					
					items: ['LEAST USED', 'LAGEST', 'LASTED ACCESSED'],
									styles: [{
											value: 'button',
											text: '按钮',
											checked: true
										},
										{
											value: 'text',
											text: '文字'
										}
								],
									current: 0,
									colorIndex: 0,
									activeColor: '#aaaaff',
									styleType: 'button'
				}
			},
			methods: {
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
							}
			},
			onBackPress() {
				// #ifdef APP-PLUS
				plus.key.hideSoftKeybord();
				// #endif
			}
		}
</script>

<style>

	
	.background{
	    position: fixed;
	    width: 100%;
	    height: 100%;
	    top: 0;
	    left: 0;
	    z-index: -1;
	}
	
	.list{
			position:absolute;
			top:380px;
			width:800rpx;
			height:630rpx;
			display:block;
			width:100%
			
		}
		
	
	
		.storage {
			position:absolute;
			height: 480rpx;
			width: 480rpx;
		right:75px;
			top:70px;
			display: block;
			margin:0 auto;
		}
	
	.选项{
		position:absolute;
		top:600rpx;
		width:100%;
	}
		.uni-common-mt {
				margin-top: 40px;
			}
</style>