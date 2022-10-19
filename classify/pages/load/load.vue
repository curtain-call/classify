<template>
	<view>
		
		
		<view class="searchInput">
			<input type="text" placeholder="请输入您的昵称"  @input="inputChanged"/>
		</view>
		
		<view class="searchbtn" @click="change">
			输入昵称   <span class="icon-search"></span>
		</view>
		
	</view>
</template>

<script>
	export default{
		data(){
			return{
		
			}
		},
		methods:{
			change(){
				
				uni.request({
					url:'http://192.168.43.98:8080/',
					method:'POST',	
					
					header: {
					  'content-type': 'application/x-www-form-urlencoded' //表明后端接收的是（表单）字符串类型，例如'id=1231454&sex=男' 
					 },
					 success: (res) => {
						 console.log(res);
						},
						complete: () => {
							console.log('请求完成');
						}
				}),
				
				
				
				
				uni.navigateBack({
			
				}),
				
				uni.showToast({
					title:'已提交您输入的昵称，请等待审核',
					icon:"none"
				})
			},
			inputChanged(e){
				if(e.target.value == ""){
					
				
				}
			}
			
		}
	}
</script>

<style>
	page{
		display: flex;
		flex-direction: column;
		background-color: #ededed;
	}
	
	.searchInput{
		width: 100%;
	}
	input{
		text-align: center;
		margin: 0 auto;
		border-radius: 10rpx;
		border: 2rpx solid #000000;
		width: 95%;
		height: 70rpx;
		margin-top: 50px;
	}
	.searchbtn{
		border-radius: 10rpx;
		background-color: #aaaaff;
		font-size: 33rpx;
		line-height: 65rpx;
		text-align: center;
		margin: 0 auto;
		margin-top: 40rpx;
		width: 35%;
		height: 65rpx;
		color: #FFFFFF;
	}
	
	.icon_searched{
			height: 100rpx;
			width: 100rpx;
		}
	
</style>
