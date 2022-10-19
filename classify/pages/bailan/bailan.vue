<template>
	<view>
		<image class="kaibai" @click="heihei()" src="../../static/bailan.png"></image>
		<text class="bailan" > 你行你来</text>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			
			heihei(){
				uni.navigateTo({
					url:'./heihei/heihei'
				})
			}
		}
	}
	
	</script>
<style>

.kaibai{
	margin:0 auto;
	margin-top: 300rpx;
	display:block;
	text-align:center;
	width:290px;
	height:270px;
	
}
.bailan{
	font-size:40rpx;
	font-weight:600;
	margin-top: 20rpx;
	text-align:center;
	display:block;
	
}
</style>
