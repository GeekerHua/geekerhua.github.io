# iOS开发小技巧
# 小技巧
记录iOS开发过程中的小技巧，绝大多数适用于OC和Swift语法语言。会不定时进行更新。

##1. TableView不显示没内容的Cell怎么办?

```objective-c
self.tableView.tableFooterView = [[UIView alloc] init];
```

## 2. 自定义了leftBarbuttonItem左滑返回手势失效了怎么办?

```objective-c
self.navigationItem.leftBarButtonItem = [[UIBarButtonItem alloc] initWithImage: img style:UIBarButtonItemStylePlain target: self action:@selector(onBack:)];
self.navigationController.interactivePopGestureRecognizer.delegate = (id)self;
```
## 3.ScrollView莫名其妙不能在viewController划到顶怎么办?
```objective-c 
self.automaticallyAdjustsScrollViewInsets = NO;
```

## 4.键盘事件写的好烦躁,都想摔键盘了,怎么办?
> 使用IQKeyboardManager

## 5.怎么在不新建一个Cell的情况下调整separaLine的位置?
```objective-c
_myTableView.separatorInset = UIEdgeInsetsMake(0, 100, 0, 0);
```

## 6.self.view就让键盘收起,
```objective-c
- (void)touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event
{
   [self.view endEditing:YES];
}
```

## 7.拉伸图片的时候怎么才能让图片不变形？
```objective-c
UIImage *image = [[UIImage imageNamed:@"xxx"] stretchableImageWithLeftCapWidth:10 topCapHeight:10];
```
