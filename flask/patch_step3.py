import re

with open("templates/ai_step3.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update the regenForm buttons
buttons_html = """          <div class="d-flex justify-content-end gap-2">
            <button type="button" id="formatBtn" class="btn-ghost-primary" style="background: var(--brand-navy); color: #fff;">
              <i class="bi bi-text-paragraph ms-2"></i> تنسيق وضبط النص الذكي
            </button>
            <button type="button" id="regenBtn" class="btn-ghost-primary">
              <i class="bi bi-arrow-repeat ms-2"></i> إعادة الصياغة
            </button>
          </div>"""
content = re.sub(
    r'<div class="d-flex justify-content-end">\s*<button type="button" id="regenBtn" class="btn-ghost-primary">.*?</button>\s*</div>',
    buttons_html,
    content,
    flags=re.DOTALL
)

# 2. Add attachments card before finalize card
attachments_card = """
      <div class="premium-form-card mb-4">
        <div class="form-header">
          <h4>المرفقات (جداول وصور)</h4>
          <p>أضف جداول أو صور هنا. سيقوم "التنسيق الذكي" بوضع علامات {{TABLE_1}} و {{IMAGE_1}} تلقائياً في النص لتحديد مكانها.</p>
        </div>
        
        <div class="mb-4">
          <label class="fw-bold mb-2" style="color: var(--brand-navy);">إضافة جدول:</label>
          <div class="table-builder-ui">
             <div class="d-flex gap-2 mb-2">
               <button type="button" class="btn btn-sm btn-outline-secondary" onclick="addCol()">+ عمود</button>
               <button type="button" class="btn btn-sm btn-outline-secondary" onclick="addRow()">+ صف</button>
               <button type="button" class="btn btn-sm btn-outline-danger" onclick="clearTable()">مسح</button>
             </div>
             <div class="table-responsive">
               <table class="table table-bordered text-center" id="dynamicTable" style="background: #fff;">
                 <tbody>
                   <tr>
                     <td><input type="text" class="form-control form-control-sm text-center" placeholder="بيانات..."></td>
                   </tr>
                 </tbody>
               </table>
             </div>
          </div>
        </div>

        <div>
          <label class="fw-bold mb-2" style="color: var(--brand-navy);">إضافة صور:</label>
          <input type="file" id="imageUploads" name="images" class="form-control" multiple accept="image/*" form="finalizeForm">
        </div>
      </div>
"""
content = content.replace('<div class="premium-form-card">\n        <div class="form-header">\n          <h4>الخطوة النهائية:', attachments_card + '\n      <div class="premium-form-card">\n        <div class="form-header">\n          <h4>الخطوة النهائية:')

# 3. Update finalize form
content = content.replace('<form action="{{ url_for(\'ai_finalize\') }}" method="post" id="finalizeForm">', '<form action="{{ url_for(\'ai_finalize\') }}" method="post" id="finalizeForm" enctype="multipart/form-data">')
content = content.replace('<input type="hidden" id="full_body_hidden" name="full_body" value="{{ full_body }}">', '<input type="hidden" id="full_body_hidden" name="full_body" value="{{ full_body }}">\n          <input type="hidden" id="table_data_hidden" name="table_data" value="[]">')

# 4. Add JS for formatting and table
js_scripts = """
  // Sync table data before submit
  document.getElementById('finalizeForm').addEventListener('submit', function() {
    const table = document.getElementById('dynamicTable');
    const rows = [];
    for(let i=0; i<table.rows.length; i++) {
        const rowData = [];
        for(let j=0; j<table.rows[i].cells.length; j++) {
            const input = table.rows[i].cells[j].querySelector('input');
            rowData.push(input ? input.value : "");
        }
        rows.push(rowData);
    }
    // Only send if it has real data (not just 1 empty cell)
    if(rows.length > 0 && rows.some(r => r.some(c => c.trim() !== ""))) {
        document.getElementById('table_data_hidden').value = JSON.stringify(rows);
    } else {
        document.getElementById('table_data_hidden').value = "[]";
    }
    
    document.getElementById('finalBtn').disabled = true;
    document.getElementById('finalBtn').innerHTML = 'جاري الإنشاء... <span class="spinner-border spinner-border-sm ms-2"></span>';
  });

  // Table Builder Functions
  function addRow() {
    const table = document.getElementById('dynamicTable').getElementsByTagName('tbody')[0];
    const cols = table.rows.length > 0 ? table.rows[0].cells.length : 1;
    const newRow = table.insertRow();
    for(let i=0; i<cols; i++) {
        const cell = newRow.insertCell(i);
        cell.innerHTML = '<input type="text" class="form-control form-control-sm text-center" placeholder="بيانات...">';
    }
  }

  function addCol() {
    const table = document.getElementById('dynamicTable').getElementsByTagName('tbody')[0];
    if(table.rows.length === 0) addRow();
    for(let i=0; i<table.rows.length; i++) {
        const cell = table.rows[i].insertCell(-1);
        cell.innerHTML = '<input type="text" class="form-control form-control-sm text-center" placeholder="بيانات...">';
    }
  }

  function clearTable() {
    const table = document.getElementById('dynamicTable').getElementsByTagName('tbody')[0];
    table.innerHTML = '<tr><td><input type="text" class="form-control form-control-sm text-center" placeholder="بيانات..."></td></tr>';
  }

  // Formatting Ajax
  document.getElementById('formatBtn').addEventListener('click', async function () {
    const btn = this;
    btn.disabled = true;
    btn.innerHTML = 'جارٍ التنسيق الذكي... <span class="spinner-border spinner-border-sm ms-2"></span>';

    try {
      const resp = await fetch("{{ url_for('api_ai_format_document') }}", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          doc_type: "{{ doc_type }}",
          sender: {{ sender|tojson|safe }},
          recipient: {{ recipient|tojson|safe }},
          subject: {{ subject|tojson|safe }},
          full_body: document.getElementById('full_body_area').value,
          has_table: document.getElementById('dynamicTable').rows.length > 1 || document.getElementById('dynamicTable').rows[0].cells.length > 1,
          has_images: document.getElementById('imageUploads').files.length > 0
        })
      });
      const data = await resp.json();
      if (data.success) {
        document.getElementById('full_body_area').value = data.full_body;
        document.getElementById('full_body_hidden').value = data.full_body;
      } else {
        alert('تعذّر التنسيق: ' + data.error);
      }
    } catch (e) {
      alert('حدث خطأ أثناء الاتصال بالخادم.');
    } finally {
      btn.disabled = false;
      btn.innerHTML = '<i class="bi bi-text-paragraph ms-2"></i> تنسيق وضبط النص الذكي';
    }
  });
"""
content = content.replace('// File upload UI removed', js_scripts)

with open("templates/ai_step3.html", "w", encoding="utf-8") as f:
    f.write(content)
