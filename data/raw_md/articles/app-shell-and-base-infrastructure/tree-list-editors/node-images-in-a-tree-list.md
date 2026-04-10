---
uid: "113215"
seealso:
- linkId: "112841"
title: Node Images in a Tree List
---
# Node Images in a Tree List

This topic describes how to show [SVG](#svg-images) or [raster](#raster-images) images for a [Tree List](xref:112837)'s entries in XAF Applications.

For this purpose, the [TreeList Editors module](xref:112841) supplies [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor). They are designed to display [](xref:DevExpress.Persistent.Base.General.ITreeNode) objects. **TreeListEditor** can also show images for the these objects. You can enable images for a Tree List's objects by implementing the [](xref:DevExpress.Persistent.Base.General.ITreeNodeSvgImageProvider) (for SVG images) or [](xref:DevExpress.Persistent.Base.General.ITreeNodeImageProvider) interface (for raster images) in a business class inherited from the **ITreeNode** interface.

> [!NOTE]
> ASP.NET Core Blazor @DevExpress.ExpressApp.Blazor.Editors.DxTreeListEditor does not support Tree Node images. 

The following image illustrates a **TreeListEditor** displaying nodes with images:

![ITreeNodeImageProvider](~/images/itreenodeimageprovider116370.png)

You can see an example in the **Feature Center** demo's **List Editors** | **Tree** | **Node Images** section. [!include[FeatureCenterLocationNote](~/templates/featurecenterlocationnote111102.md)]

> [!NOTE]
> Use either SVG or raster images for all items in one collection. When using SVG and raster images simultaneously, a Tree List editor can fail to show certain images. In this case, make sure image files for all entries have the same format, and check the application's Log File for an additional diagnostic message.

## SVG Images 

This section demonstrates implementing the [](xref:DevExpress.Persistent.Base.General.ITreeNodeSvgImageProvider) interface and using its [GetSvgImage](xref:DevExpress.Persistent.Base.General.ITreeNodeSvgImageProvider.GetSvgImage(System.String@)) method to display SVG images for a Tree List's objects.

The following code snippet shows how the **Product** business class implements the **ITreeNodeSvgImageProvider** interface. If a **Product** object does not have nested products, then the **GetSvgImage** method returns the "BO_Product" image. Otherwise, the "BO_Category" image is returned. The [ImageLoader.GetImageInfo](xref:DevExpress.ExpressApp.Utils.ImageLoader.GetImageInfo*) method retrieves these images from XAF's [standard image library](xref:404201).


# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.Utils;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.Base.General;
using DevExpress.Persistent.BaseImpl.EF;
using System.Collections.ObjectModel;
using System.ComponentModel;
//...
[DefaultClassOptions]
public class ProductImg : BaseObject, ITreeNode, ITreeNodeSvgImageProvider {
    public virtual string Caption { get; set; }
    [Browsable(false)]
    public virtual ProductImg ParentProduct { get; set; }
    [DevExpress.ExpressApp.DC.Aggregated]
    public virtual ObservableCollection<ProductImg> NestedProducts { get; set; } = new ObservableCollection<ProductImg>();

    #region ITreeNode Members
    IBindingList ITreeNode.Children {
        get { return new BindingList<ProductImg>(NestedProducts); }
    }
    string ITreeNode.Name {
        get { return Caption; }
    }
    ITreeNode ITreeNode.Parent {
        get { return ParentProduct; }
    }
    #endregion

    #region ITreeNodeSvgImageProvider Members
    public DevExpress.Utils.Svg.SvgImage GetSvgImage(out string imageName) {
        if(NestedProducts != null && NestedProducts.Count > 0) {
            imageName = "BO_Category";
        } else {
            imageName = "BO_Product";
        }
        return ImageLoader.Instance.GetImageInfo(imageName).CreateSvgImage();
    }
    #endregion
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.Utils;
using DevExpress.Persistent.Base.General;
//...
public class Product : BaseObject, ITreeNode, ITreeNodeSvgImageProvider {
    private Product parentProduct;
    private string caption;

    public Product(Session session) : base(session) { }

    public string Caption {
        get { return caption; }
        set { SetPropertyValue<string>(nameof(Caption), ref caption, value); }
    }
    [Browsable(false)]
    [Association("Product-Product")]
    public Product ParentProduct {
        get { return parentProduct; }
        set { SetPropertyValue<Product>(nameof(ParentProduct), ref parentProduct, value); }
    }
    [Association("Product-Product"), Aggregated]
    public XPCollection<Product> NestedProducts {
        get { return GetCollection<Product>(nameof(NestedProducts)); }
    }

    #region ITreeNode Members
    IBindingList ITreeNode.Children {
        get { return NestedProducts; }
    }
    string ITreeNode.Name {
        get { return Caption; }
    }
    ITreeNode ITreeNode.Parent {
        get { return ParentProduct; }
    }
    #endregion

    #region ITreeNodeSvgImageProvider Members
    public DevExpress.Utils.Svg.SvgImage GetSvgImage(out string imageName) {
        if (NestedProducts != null && NestedProducts.Count > 0) {            
            imageName = "BO_Category";
        }
        else {
            imageName = "BO_Product";
        }
        return ImageLoader.Instance.GetImageInfo(imageName).CreateSvgImage();
    }
    #endregion 
}
```
***

## Raster Images

You can use the same approach for raster images, but implement the [](xref:DevExpress.Persistent.Base.General.ITreeNodeImageProvider) instead. Then replace the **GetSvgImage** method with the **ITreeNodeImageProvider**'s [ITreeNodeImageProvider.GetImage](xref:DevExpress.Persistent.Base.General.ITreeNodeImageProvider.GetImage(System.String@)) method as shown below.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
public class Product : BaseObject, ITreeNode, ITreeNodeImageProvider {
    // ...
    #region ITreeNodeImageProvider Members
    public DXImage GetImage(out string imageName) {
        if (NestedProducts != null && NestedProducts.Count > 0) {            
            imageName = "BO_Category";
        }
        else {
            imageName = "BO_Product";
        }
        return ImageLoader.Instance.GetImageInfo(imageName).Image;
    }
    #endregion
}   

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
public class Product : BaseObject, ITreeNode, ITreeNodeImageProvider {
    // ...
    #region ITreeNodeImageProvider Members
    public DXImage GetImage(out string imageName) {
        if (NestedProducts != null && NestedProducts.Count > 0) {            
            imageName = "BO_Category";
        }
        else {
            imageName = "BO_Product";
        }
        return ImageLoader.Instance.GetImageInfo(imageName).Image;
    }
    #endregion
}   
```
***

