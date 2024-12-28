from tilemap import TileMap, providers

# 定义瓦片提供服务商信息，以及瓦片存储位置
tile = TileMap(provider=providers.Amap.Satellite, cache_folder='./tiles')

# 需要获取瓦片额范围
west, south, east, north = (
    113.93329, 22.57102,
    113.94413, 22.58131
)

# zoom 下载瓦片的级别，ll 表示 [west, south, east, north] 输入为经纬度
tile.bounds2img(west, south, east, north, zoom=18, ll=True)
