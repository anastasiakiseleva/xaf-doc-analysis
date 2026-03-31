---
uid: "113659"
seealso: []
title: Color Properties in XPO
---
# Color Properties in XPO

This topic demonstrates two approaches to store a `System.Drawing.Color` property value in the database managed by the **XPO** ORM.

1. The first approach is to implement a **Value Converter**.
	
	```csharp
	using System;
	using System.Drawing;
	using DevExpress.Xpo.Metadata;
	// ...
	public class ColorValueConverter : ValueConverter {
        public override object ConvertFromStorageType(object obj) {
            if(obj == null) {
                return null;
            }
            return Color.FromArgb((Int32)obj);
        }
        public override object ConvertToStorageType(object obj) {
            if(obj == null) {
                return null;
            }
            return ((Color)obj).ToArgb();
        }
        public override Type StorageType {
            get { return typeof(Int32); }
        }
    }
	```
	
	After that, decorate properties that  need to be converted with the [](xref:DevExpress.Xpo.ValueConverterAttribute) and the converter will be called on each attempt to store or acquire a value of the @System.Drawing.Color type.
	
	```csharp
	using DevExpress.Xpo;
	using System.Drawing;
	//...
	private Color color;
	[ValueConverter(typeof(ColorValueConverter))]
	public Color Color {
	    get { return color; }
	    set { SetPropertyValue(nameof(Color), ref color, value); }
	}
	```

2. Another approach is to convert the @System.Drawing.Color type to @System.Int32 on property implementation using `get` and `set` accessors, as shown below.
	
	```csharp
	using DevExpress.Xpo;
	using System.Drawing;
	//...
	[Persistent("Color")]
	private Int32 color;
	[NonPersistent]
	public Color Color {
	    get { return Color.FromArgb(color); }
	    set {
	        color = value.ToArgb();
	        OnChanged(nameof(Color));
	    }
	}
	```

	> [!NOTE]
	> If the type's class does not have an appropriate conversion method ([Color.ToArgb](https://learn.microsoft.com/en-us/dotnet/api/system.drawing.color.toargb#System_Drawing_Color_ToArgb) in this case), [implement a Type Converter](https://learn.microsoft.com/en-us/previous-versions/ayybcxe5(v=vs.140)) and use it any time you need a value conversion between the type you need to store and an ORM-friendly type.
