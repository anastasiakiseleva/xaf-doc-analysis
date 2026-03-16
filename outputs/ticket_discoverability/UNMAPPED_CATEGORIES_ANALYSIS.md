# UNMAPPED Support Ticket Categories - XAF Documentation Analysis

## Analysis Date: February 13, 2026
## Source: DevExpress Documentation Search (dxdocs MCP)

---

## Executive Summary

Analyzed 4 UNMAPPED support ticket categories (447 tickets total) to determine how they are covered in XAF documentation and recommend appropriate concept mappings in concepts.yml.

**Key Finding**: 3 of 4 categories have clear XAF documentation coverage and can be mapped to existing concepts. 1 category ("TIME") is a meta-category about documentation effort estimation, not an actual XAF feature.

---

## Category Analysis

### 1. Form Templates (207 tickets - **46% of unmapped tickets**)

#### Documentation Coverage
**Doc Topic**: "Blazor Application Templates" and "WinForms Application Templates"  
**URL**: https://docs.devexpress.com/eXpressAppFramework/112609

#### What It Is
XAF uses built-in **Application Templates** (not form templates) that define the appearance and layout of Windows and Frames. These are controls that implement `IFrameTemplate` or `IWindowTemplate` interfaces.

**Template Types**:
- **Main Window Templates**: ApplicationWindowTemplate, MainRibbonFormV2, LightStyleMainForm
- **Detail View Templates**: DetailFormTemplate, DetailRibbonFormV2
- **Popup Templates**: PopupForm, PopupWindowTemplate
- **Nested Frame Templates**: NestedFrameTemplate
- **Lookup Templates**: LookupForm, LookupControlTemplate

#### Key Documentation Sections
1. Template architecture and interfaces
2. Built-in template types (Blazor & WinForms)
3. Template customization via Model Editor
4. Custom template creation
5. Template context (ApplicationWindow, View, PopupWindow, NestedFrame, etc.)

#### Related APIs
- `XafApplication.CreateTemplate()`
- `IFrameTemplate`, `IWindowTemplate`
- `TemplateContext` enum values
- `IModelOptionsWin.FormStyle`, `IModelOptionsBlazor.FormStyle`

#### User Language
- "form templates"
- "window templates"
- "detail form"
- "main form"
- "ribbon form"
- "template customization"
- "layout templates"

#### Recommendation
**Create new concept**: "Application Templates"

**Mapping**: 
```yaml
- name: Application Templates
  type: ui
  parent: null
  synonyms:
    - Form Templates  # User language from tickets
    - Window Templates
    - Frame Templates
    - IFrameTemplate
    - IWindowTemplate
    - DetailFormTemplate
    - MainFormTemplate
    - PopupForm
    - ApplicationWindowTemplate
    - Detail Form Template
    - Main Window Template
    - Ribbon Form Template
    - Template Customization
    - Custom Templates
  tags: [ui, architecture, windows]
  description: Built-in controls that define the appearance and layout of windows and frames in XAF applications
```

**Rationale**: This is a distinct architectural concept separate from Views or Layout. It deserves its own concept node.

---

### 2. Popups (144 tickets - **32% of unmapped tickets**)

#### Documentation Coverage
**Doc Topic**: Multiple articles on popup windows and dialogs  
**Primary URLs**: 
- https://docs.devexpress.com/eXpressAppFramework/112805 (Dialog Controller)
- https://docs.devexpress.com/eXpressAppFramework/118240 (Confirmation Dialogs)
- https://docs.devexpress.com/eXpressAppFramework/404014 (Adjust Popup Size)

#### What It Is
Functionality for displaying views in popup/modal windows using:
- `ShowViewInPopupWindow()` method
- `ShowViewParameters` with `TargetWindow.NewModalWindow`
- `DialogController` for OK/Cancel buttons
- `PopupWindowShowAction` for action-triggered popups
- `TemplateContext.PopupWindow` for popup-specific templates

#### Key Documentation Sections
1. ShowViewInPopupWindow method usage
2. ShowViewParameters configuration
3. Dialog Controller usage
4. PopupWindowShowAction customization
5. Popup size and style customization
6. OK/Cancel button handling

#### Related APIs
- `ShowViewStrategyBase.ShowViewInPopupWindow()`
- `ShowViewParameters.TargetWindow`, `.Context`
- `DialogController.AcceptAction`, `.CancelAction`
- `PopupWindowShowAction.CustomizePopupWindowParams`
- `CustomizePopupWindowParamsEventArgs`

#### User Language
- "popups"
- "popup windows"
- "modal dialogs"
- "dialog windows"
- "show popup"
- "modal windows"

#### Recommendation
**Map to existing concept**: "Popup Windows"

**Add synonyms**:
```yaml
- name: Popup Windows
  type: ui
  parent: Views
  synonyms:
    # ... existing synonyms ...
    - Popups  # Add this - direct match to ticket category
    - Show Popup
    - Popup Window Size
    - Popup Style
```

**Rationale**: The "Popup Windows" concept already exists and covers this functionality. Simple synonym addition needed.

---

### 3. Callbacks (66 tickets - **15% of unmapped tickets**)

#### Documentation Coverage
**Doc Topic**: Limited - primarily ASP.NET Web Forms specific  
**Found**: Code examples with `ASPxWebControl.CallbackError`, `XafCallbackManager.GetScript()`

#### What It Is
**Legacy ASP.NET Web Forms feature** for client-server callbacks in Web applications. **Not applicable** to modern Blazor or Web API applications.

**Limited Usage**:
- `XafCallbackManager` - ASP.NET Web Forms callback management
- `ASPxWebControl.CallbackError` event handling
- Client-side callbacks for custom actions in Web Forms UI

#### Key Documentation Sections
- Minimal conceptual documentation
- Primarily found in code examples for Web Forms customizations
- Part of DevExpress ASP.NET Web Forms control callback infrastructure

#### Related APIs
- `XafCallbackManager.GetScript()`
- `ASPxWebControl.CallbackError` event
- Action callback handling in Web Forms

#### User Language
- "callbacks"
- "server callbacks"
- "callback errors"
- "ASPx callbacks"

#### Recommendation
**Option 1 - Create minimal concept** (if significant Web Forms usage):
```yaml
- name: Web Forms Callbacks
  type: platform
  parent: null  # Or could be child of "WinForms" (though it's actually Web Forms)
  synonyms:
    - Callbacks
    - ASPx Callbacks
    - Server Callbacks
    - XafCallbackManager
    - Callback Errors
    - Client Callbacks
  tags: [web-forms, legacy, asp.net]
  description: Legacy ASP.NET Web Forms callback mechanism for client-server communication in XAF Web applications
```

**Option 2 - Map to platform concept** (recommended):
Map to existing platform concept since this is platform-specific functionality, not a general XAF concept. Add note in ".NET Runtime" or create "ASP.NET Web Forms" concept if one exists.

**Rationale**: This is legacy platform-specific functionality with minimal documentation. Only create dedicated concept if significant ticket volume continues.

---

### 4. TIME: 1-2h (tech part + time to write text) (30 tickets - **7% of unmapped tickets**)

#### Documentation Coverage
**None** - This is NOT an XAF feature.

#### What It Is
**Meta-category**: This appears to be an internal DevExpress support ticket category for tracking **documentation effort estimation**, not actual user-facing technical content.

The category name "TIME: 1-2h (tech part + time to write text)" suggests:
- Time estimate for creating documentation
- Internal workflow/project management category
- Not related to any XAF functionality

#### Search Results Analysis
Search for "time tracking time estimation task duration" returned:
- Task management examples (DueDate, StartDate properties)
- Business object examples for project management
- No actual XAF framework feature called "TIME"

#### Recommendation
**Do NOT create concept** - This is an internal categorization artifact, not a documentable XAF concept.

**Action**: Investigate ticket contents to understand if these are mis-categorized tickets that should be reassigned to proper feature categories.

---

## Summary Recommendations

| Category | Ticket Count | Action | Priority |
|----------|--------------|--------|----------|
| **Form Templates** | 207 (46%) | CREATE new concept "Application Templates" | HIGH |
| **Popups** | 144 (32%) | ADD synonyms to existing "Popup Windows" | MEDIUM |
| **Callbacks** | 66 (15%) | CREATE minimal "Web Forms Callbacks" concept OR map to platform | LOW |
| **TIME** | 30 (7%) | NO CONCEPT - Investigate ticket mis-categorization | LOW |

### Implementation Priority
1. **High Priority**: Create "Application Templates" concept (207 tickets)
2. **Medium Priority**: Add "Popups" synonym to "Popup Windows" (144 tickets)
3. **Low Priority**: Decide on Callbacks handling based on Web Forms app usage (66 tickets)
4. **Investigation**: Review TIME category tickets for proper categorization (30 tickets)

### Expected Impact
- **351 tickets** (78.5% of unmapped) can be immediately mapped with these changes
- **66 tickets** (14.8%) need platform strategy decision
- **30 tickets** (6.7%) need investigation/recategorization

---

## Detailed Concept Definitions

### Proposed: Application Templates Concept

```yaml
- name: Application Templates
  type: ui
  parent: null
  synonyms:
    - Form Templates
    - Window Templates
    - Frame Templates
    - IFrameTemplate
    - IWindowTemplate
    - DetailFormTemplate
    - MainFormTemplate
    - PopupForm
    - ApplicationWindowTemplate
    - MainRibbonFormV2
    - DetailRibbonFormV2
    - NestedFrameTemplate
    - LookupForm
    - LookupControlTemplate
    - LogonWindowTemplate
    - Detail Form Template
    - Main Window Template
    - Ribbon Form Template
    - Template Customization
    - Custom Templates
    - Form Designer
    - Window Layout
    - TemplateContext
    - CreateTemplate
  tags: [ui, architecture, windows, customization]
  description: Built-in controls that define the appearance and layout of windows and frames in XAF applications, implementing IFrameTemplate or IWindowTemplate interfaces
```

### Updated: Popup Windows Concept

```yaml
- name: Popup Windows
  type: ui
  parent: Views
  synonyms:
    - Popup Views
    - Modal Windows
    - Dialog Windows
    - ShowViewInPopupWindow
    - Popup Dialog
    - Modal Popup
    - Dialog View
    - Popups  # ADD THIS
    - Show Popup  # ADD THIS
    - Popup Window Size  # ADD THIS
    - Popup Style  # ADD THIS
    - Modal Dialog
    - NewModalWindow
  tags: [ui, views, dialogs]
  description: Displaying views in popup windows or modal dialogs with ShowViewInPopupWindow method
```

### Optional: Web Forms Callbacks Concept

```yaml
- name: Web Forms Callbacks
  type: platform
  parent: null
  synonyms:
    - Callbacks
    - ASPx Callbacks
    - Server Callbacks
    - XafCallbackManager
    - CallbackError
    - Client Callbacks
    - Callback Manager
    - ASPxWebControl Callback
  tags: [web-forms, legacy, asp.net, platform-specific]
  description: Legacy ASP.NET Web Forms callback mechanism for client-server communication in XAF Web applications (deprecated in favor of Blazor)
```

---

## Next Steps

1. **Review and approve** these concept definitions
2. **Implement** Application Templates concept (high priority)
3. **Update** Popup Windows with new synonyms (medium priority)
4. **Decide** on Callbacks approach based on Web Forms application usage
5. **Investigate** TIME category tickets for proper recategorization
6. **Re-run** analyze_real_tickets.py to measure improvement
7. **Validate** mappings with support team domain experts

---

## Validation Queries for dxdocs

If further validation needed, search for:
- "IFrameTemplate IWindowTemplate template architecture"
- "MainFormV2 DetailFormV2 WinForms templates"
- "ShowViewParameters NewModalWindow popup"
- "DialogController AcceptAction CancelAction"
- "XafCallbackManager Web Forms ASPx"

## Documentation URLs Referenced

### Form Templates / Application Templates
- https://docs.devexpress.com/eXpressAppFramework/112609 (Templates overview)
- https://docs.devexpress.com/eXpressAppFramework/403450 (Blazor Templates)
- https://docs.devexpress.com/eXpressAppFramework/403446 (WinForms Templates)
- https://docs.devexpress.com/eXpressAppFramework/112696 (Template Customization)
- https://docs.devexpress.com/eXpressAppFramework/112618 (Create Custom Ribbon Template)

### Popups
- https://docs.devexpress.com/eXpressAppFramework/112805 (Dialog Controller)
- https://docs.devexpress.com/eXpressAppFramework/118240 (Confirmation Dialogs)
- https://docs.devexpress.com/eXpressAppFramework/404014 (Adjust Popup Size)
- https://docs.devexpress.com/eXpressAppFramework/112803 (Ways to Show a View)

### Callbacks
- Limited coverage - primarily code examples in Web Forms context

---

**Analysis completed by**: GitHub Copilot  
**Data source**: DevExpress Documentation (dxdocs MCP)  
**Methodology**: Semantic search across eXpressAppFramework documentation with ticket category terms
