---
uid: "113660"
title: Color Properties in EF Core
seealso:  
- linkId: "117395"
---
# Color Properties in EF Core

The following example demonstrates how to store a **System.Drawing.Color** property value in the EF Core-based database. Use the EF Core Value Converter to convert the **System.Drawing.Color** type to the **System.Int32**:

# [C#](#tab/tabid-csharp)

```csharp
using System.ComponentModel.DataAnnotations.Schema;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using System.Drawing;

public class BusinessObject : BaseObject {
    // ...    
    public virtual Color Color { get; set; }
}

class DataContext : DbContext {
    // ...
    public DbSet<BusinessObject> BusinessObjects { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder) {
        // ...
        modelBuilder.Entity<BusinessObject>()
            .Property(t => t.Color)
            .HasConversion<ColorToInt32Converter>();
    }
}

class ColorToInt32Converter : ValueConverter<Color, int> {
    public ColorToInt32Converter()
        : base(c => c.ToArgb(), v => Color.FromArgb(v)) { }
}
```

***

This technique uses the [Microsoft ValueConverter Class](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.storage.valueconversion.valueconverter) to convert **Color** values to **Int32** and vice versa.
