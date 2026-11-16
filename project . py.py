import webbrowser

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Career Guidance Pro</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        * { font-family: 'Poppins', sans-serif; box-sizing: border-box; }
        body { background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 100%); background-size: 400% 400%; animation: gradient 15s ease infinite; min-height: 100vh; padding: 40px 20px; margin: 0; }
        @keyframes gradient { 0%{background-position:0% 50%} 50%{background-position:100% 50%} 100%{background-position:0% 50%} }
        
        h1 { text-align: center; color: white; font-size: 42px; font-weight: 800; text-shadow: 0 5px 15px rgba(0,0,0,0.3); margin-bottom: 10px; }
        .subtitle { text-align: center; color: rgba(255,255,255,0.9); font-size: 16px; margin-bottom: 30px; }
        
        .card { background: rgba(255,255,255,0.15); padding: 35px; margin: 25px auto; border-radius: 25px; max-width: 750px; box-shadow: 0 20px 60px rgba(0,0,0,0.3); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.2); animation: slideUp 0.8s; }
        @keyframes slideUp { from {opacity:0; transform: translateY(40px);} to {opacity:1; transform: translateY(0);} }
        
        h2 { color: white; font-size: 22px; margin-bottom: 18px; display: flex; align-items: center; gap: 10px; }
        .form-group { margin-bottom: 18px; }
        label { color: white; font-weight: 600; display: block; margin-bottom: 8px; }
        input, select { width: 100%; padding: 15px; border: 2px solid rgba(255,255,255,0.3); border-radius: 15px; background: rgba(255,255,0.9); font-size: 15px; transition: 0.3s; }
        input:focus, select:focus { border-color: #f093fb; outline: none; box-shadow: 0 0 0 4px rgba(240,147,251,0.3); background: white; }
        
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
        
        button { background: linear-gradient(90deg, #f093fb, #f5576c); color: white; padding: 16px; border: none; border-radius: 15px; width: 100%; font-size: 18px; font-weight: 700; cursor: pointer; transition: 0.3s; box-shadow: 0 8px 20px rgba(245,87,108,0.4); }
        button:hover { transform: translateY(-4px); box-shadow: 0 12px 30px rgba(245,87,108,0.6); }
        
        .hidden { display: none; }
        .badge { background: linear-gradient(90deg, #667eea, #764ba2); color: white; padding: 10px 18px; border-radius: 30px; display: inline-block; margin: 6px; font-size: 14px; font-weight: 600; box-shadow: 0 4px 10px rgba(0,0,0,0.2); }
        .salary { font-size: 26px; color: #10b981; font-weight: 800; text-shadow: 0 2px 5px rgba(16,185,129,0.3); }
        
        .info-box { background: rgba(255,255,255,0.9); padding: 20px; border-radius: 18px; margin: 15px 0; color: #1f2937; }
        .info-box a { color: #667eea; text-decoration: none; font-weight: 600; }
        .info-box a:hover { text-decoration: underline; }
        .stat { text-align: center; padding: 15px; background: rgba(255,255,255,0.2); border-radius: 15px; }
        .stat h3 { margin: 0; font-size: 28px; color: white; }
        .stat p { margin: 5px 0 0 0; color: rgba(255,255,255,0.9); font-size: 14px; }
        .stats-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin: 20px 0; }
        li { margin: 8px 0; }
    </style>
</head>
<body>
    <h1>🚀 CAREER GUIDANCE PRO</h1>
    <p class="subtitle">AI Powered Career Report in 30 Seconds</p>
    
    <div class="card" id="form">
        <h2>📝 Tell Us About You</h2>
        <div class="grid">
            <div class="form-group">
                <label>👤 Full Name</label>
                <input type="text" id="name" placeholder="Enter your name" required>
            </div>
            <div class="form-group">
                <label>🎂 Age</label>
                <input type="number" id="age" placeholder="18" required>
            </div>
        </div>
        <div class="grid">
            <div class="form-group">
                <label>🎓 Branch</label>
                <input type="text" id="branch" placeholder="B.Tech CSE" required>
            </div>
            <div class="form-group">
                <label>📊 CGPA</label>
                <input type="text" id="cgpa" placeholder="8.5" required>
            </div>
        </div>
        
        <div class="form-group">
            <label>🎯 Main Interest</label>
            <select id="interest" onchange="showSubInterest()" required>
                <option value="">Select Interest</option>
                <option value="AI">🤖 AI & Data Science</option>
                <option value="Coding">💻 Software & Coding</option>
                <option value="Cyber Security">🔒 Cyber Security</option>
                <option value="Design">🎨 UI/UX Design</option>
                <option value="Business">📈 Business & Management</option>
            </select>
        </div>

        <div class="form-group hidden" id="sub_ai_box">
            <label>🤖 AI Specialization</label>
            <select id="sub_ai">
                <option value="">Select Field</option>
                <option value="Python">🐍 Python for AI</option>
                <option value="Machine Learning">🧠 Machine Learning</option>
                <option value="Data Science">📊 Data Science</option>
            </select>
        </div>

        <div class="form-group hidden" id="sub_coding_box">
            <label>💻 Coding Specialization</label>
            <select id="sub_coding">
                <option value="">Select Field</option>
                <option value="Web Development">🌐 Web Development</option>
                <option value="App Development">📱 App Development</option>
                <option value="DSA">⚡ DSA & Problem Solving</option>
            </select>
        </div>
        
        <button onclick="makeReport()">✨ Generate My AI Report</button>
    </div>

    <div class="card" id="report" style="display:none;">
        <h2>👤 Your Profile</h2>
        <div class="info-box">
            <b style="font-size:20px;"><span id="n"></span></b> • <span id="a"></span> yrs • <span id="b"></span> • CGPA: <span id="c"></span>
        </div>
        
        <div class="stats-grid">
            <div class="stat"><h3 id="career_short"></h3><p>Career Role</p></div>
            <div class="stat"><h3>90</h3><p>Days Roadmap</p></div>
            <div class="stat"><h3>5+</h3><p>Skills Needed</p></div>
        </div>
        
        <h2>🎯 Career Path</h2>
        <div class="info-box">
            <p><b>Interest:</b> <span id="i"></span></p>
            <p><b>Specialization:</b> <span id="sub"></span></p>
            <p><b>Role:</b> <span id="career"></span></p>
            <p class="salary">💰 <span id="salary"></span></p>
        </div>

        <h2>📖 Why This Field?</h2>
        <p style="color:white; line-height:1.8;" id="about"></p>
        
        <h2>🛠️ Top Skills</h2>
        <div id="skills"></div>

        <h2>📍 Your 90 Day Roadmap</h2>
        <div class="info-box"><ol id="roadmap"></ol></div>

        <h2>📚 Best Courses</h2>
        <div class="info-box" id="courses"></div>

        <h2>💡 Project Ideas</h2>
        <div class="info-box"><ul id="projects"></ul></div>

        <h2>📜 Certifications</h2>
        <div class="info-box" id="certs"></div>

        <h2>❓ Interview Questions</h2>
        <div class="info-box"><ul id="questions"></ul></div>

        <h2>💼 Hiring Companies</h2>
        <p style="color:white; font-weight:600;" id="companies"></p>

        <button onclick="window.print()">🖨️ Download PDF Report</button>
        <button onclick="location.reload()" style="margin-top:12px; background: linear-gradient(90deg, #6b7280, #4b5563);">🔄 Start New</button>
    </div>

<script>
function showSubInterest(){
    let interest = document.getElementById("interest").value;
    document.getElementById("sub_ai_box").classList.add("hidden");
    document.getElementById("sub_coding_box").classList.add("hidden");
    if(interest == "AI") document.getElementById("sub_ai_box").classList.remove("hidden");
    if(interest == "Coding") document.getElementById("sub_coding_box").classList.remove("hidden");
}

function makeReport(){
    let name = document.getElementById("name").value;
    let age = document.getElementById("age").value;
    let branch = document.getElementById("branch").value;
    let cgpa = document.getElementById("cgpa").value;
    let interest = document.getElementById("interest").value;
    let sub = "";
    
    let data = {};
    
    if(interest == "AI"){
        sub = document.getElementById("sub_ai").value;
        if(sub == "Python"){
            data = {
                career_short: "AI Dev", career: "Python AI Developer", salary: "₹6 LPA - ₹18 LPA", 
                about: "Python AI Developer machine learning models banata hai. ChatGPT, Alexa, Self-driving car sab Python se hi bante hain. Ye 2030 tak ki sabse high demand job hai.",
                skills: ["Python", "NumPy & Pandas", "TensorFlow", "OpenCV", "Scikit-learn"], 
                roadmap: ["Month 1: Python + OOP + NumPy + 2 Projects", "Month 2: Machine Learning + Kaggle Competitions", "Month 3: Deep Learning + Portfolio Website + GitHub"], 
                courses: ["<a href='#' target='_blank'>Coursera: Python for Everybody</a>", "<a href='#' target='_blank'>Udemy: Complete Python Bootcamp</a>", "<a href='#' target='_blank'>YouTube: CodeWithHarry Python</a>"],
                projects: ["Chatbot using NLP", "Face Recognition System", "Stock Price Prediction"],
                certs: ["Google AI Certificate", "IBM Data Science Professional", "Microsoft Azure AI Fundamentals"],
                questions: ["What is overfitting?", "Explain Train-Test Split", "What are Neural Networks?"],
                companies: "Google, Microsoft, Amazon, TCS, Infosys, Startups" 
            };
        }
        if(sub == "Machine Learning"){
            data = {
                career_short: "ML Eng", career: "ML Engineer", salary: "₹8 LPA - ₹25 LPA", 
                about: "ML Engineer data se seekh kar machine ko smart banata hai. YouTube recommendation, Fraud detection, Face unlock sab ML hai.",
                skills: ["Python", "Statistics", "TensorFlow", "Data Analysis", "MLOps"], 
                roadmap: ["Month 1: Python + Statistics + Pandas", "Month 2: ML Algorithms + 3 End-to-End Projects", "Month 3: Model Deployment + Kaggle + Portfolio"], 
                courses: ["<a href='#' target='_blank'>Coursera: ML by Andrew Ng</a>", "<a href='#' target='_blank'>Kaggle Learn Courses</a>"],
                projects: ["Movie Recommendation System", "Spam Email Classifier", "House Price Predictor"],
                certs: ["TensorFlow Developer Certificate", "AWS ML Specialty"],
                questions: ["Difference between Bagging and Boosting?", "What is ROC Curve?", "Explain Cross Validation"],
                companies: "Google, Meta, Flipkart, Swiggy, Zomato, Razorpay" 
            };
        }
        if(sub == "Data Science"){
            data = {
                career_short: "Data Sci", career: "Data Scientist", salary: "₹7 LPA - ₹22 LPA", 
                about: "Data Scientist company ke bade data ko samajh kar business decision leta hai. Har badi company ko Data Scientist chahiye.",
                skills: ["Python", "SQL", "Pandas", "Tableau", "Statistics"], 
                roadmap: ["Month 1: Python + SQL + Excel", "Month 2: Data Analysis + Data Visualization", "Month 3: Case Studies + Portfolio + Interview Prep"], 
                courses: ["<a href='#' target='_blank'>DataCamp Data Science Track</a>", "<a href='#' target='_blank'>Udemy: Python for Data Science</a>"],
                projects: ["Sales Data Dashboard", "Customer Segmentation", "COVID-19 Data Analysis"],
                certs: ["Google Data Analytics Certificate", "IBM Data Scientist Professional"],
                questions: ["What is P-Value?", "Explain A/B Testing", "Difference between Correlation and Causation"],
                companies: "Accenture, Deloitte, IBM, Paytm, PhonePe, Flipkart" 
            };
        }
    }
    
    if(interest == "Coding"){
        sub = document.getElementById("sub_coding").value;
        if(sub == "Web Development"){
            data = {
                career_short: "Web Dev", career: "Full Stack Web Developer", salary: "₹4 LPA - ₹15 LPA", 
                about: "Web Developer websites aur web apps banata hai. Amazon, Flipkart, Instagram sab isi se bante hain.",
                skills: ["HTML", "CSS", "JavaScript", "React", "Node.js"], 
                roadmap: ["Month 1: HTML CSS JS + 3 Websites", "Month 2: React + Node.js + Database", "Month 3: 2 Full Stack Projects + Deployment"], 
                courses: ["<a href='#' target='_blank'>Udemy: Complete Web Dev Bootcamp</a>", "<a href='#' target='_blank'>freeCodeCamp</a>"],
                projects: ["E-commerce Website", "Portfolio Website", "Blog with Admin Panel"],
                certs: ["Meta Front-End Developer", "AWS Cloud Practitioner"],
                questions: ["What is REST API?", "Explain React Hooks", "What is CORS?"],
                companies: "TCS, Wipro, HCL, Startups, Product Companies" 
            };
        }
        if(sub == "App Development"){
            data = {
                career_short: "App Dev", career: "Mobile App Developer", salary: "₹5 LPA - ₹16 LPA", 
                about: "App Developer Android aur iOS ke liye apps banata hai. Jaise Zomato, Instagram, Games.",
                skills: ["Flutter", "Dart", "React Native", "Firebase", "UI Design"], 
                roadmap: ["Month 1: Flutter Basics + 2 Apps", "Month 2: Firebase + APIs + State Management", "Month 3: 1 Play Store App + Monetization"], 
                courses: ["<a href='#' target='_blank'>Udemy: Flutter & Dart</a>", "<a href='#' target='_blank'>React Native Docs</a>"],
                projects: ["Todo App with Firebase", "Food Delivery App UI", "Chat Application"],
                certs: ["Google Associate Android Developer"],
                questions: ["What is State Management?", "Difference between Native and Hybrid", "How to optimize app performance?"],
                companies: "Google, Uber, Dream11, CRED, Startups, Freelance" 
            };
        }
        if(sub == "DSA"){
            data = {
                career_short: "SWE", career: "Software Engineer", salary: "₹8 LPA - ₹30 LPA", 
                about: "Software Engineer product banata hai aur coding problems solve karta hai. FAANG companies me isi ki sabse zyada demand hai.",
                skills: ["C++", "Java", "DSA", "System Design", "Git"], 
                roadmap: ["Month 1: DSA Basics + 100 Problems", "Month 2: 200+ LeetCode + OOP", "Month 3: System Design + Mock Interviews"], 
                courses: ["<a href='#' target='_blank'>Striver's DSA Sheet</a>", "<a href='#' target='_blank'>LeetCode Premium</a>"],
                projects: ["Library Management System", "Chat App with Socket", "URL Shortener"],
                certs: ["Oracle Java Certification"],
                questions: ["Explain HashMap vs HashSet", "What is Time Complexity?", "Design Instagram Feed"],
                companies: "Google, Amazon, Microsoft, Adobe, ServiceNow, Atlassian" 
            };
        }
    }

    if(interest == "Cyber Security"){
        data = {
            career_short: "Sec Analyst", career: "Cyber Security Analyst", salary: "₹5 LPA - ₹20 LPA", 
            about: "Company ke system, website aur data ko hackers se bachata hai. Ethical hacking iska part hai.",
            skills: ["Linux","Networking","Ethical Hacking","Wireshark","Python"], 
            roadmap: ["Month 1: Linux + Networking Fundamentals","Month 2: Ethical Hacking Tools + Practice","Month 3: Bug Bounty + CEH Certification"], 
            courses: ["<a href='#' target='_blank'>TryHackMe</a>", "<a href='#' target='_blank'>HackTheBox Academy</a>"],
            projects: ["Network Scanner", "Password Cracker", "Vulnerability Assessment"],
            certs: ["CEH - Certified Ethical Hacker", "CompTIA Security+"],
            questions: ["What is SQL Injection?", "Explain DDoS Attack", "What is Firewall?"],
            companies: "IBM, Cisco, QuickHeal, Govt Jobs, Banks" 
        };
    }
    if(interest == "Design"){
        data = {
            career_short: "UI/UX", career: "UI/UX Designer", salary: "₹4 LPA - ₹14 LPA", 
            about: "Apps aur websites ko sundar aur easy to use banata hai. Har product ki pehli impression design se hi aati hai.",
            skills: ["Figma","Adobe XD","UI Design","Prototyping","User Research"], 
            roadmap: ["Month 1: Figma Basics + Design Principles","Month 2: UI Projects + Case Studies","Month 3: Portfolio Website + Dribbble"], 
            courses: ["<a href='#' target='_blank'>Google UX Design Certificate</a>", "<a href='#' target='_blank'>Coursera: UI/UX Design</a>"],
            projects: ["Redesign Zomato App", "Banking App UI", "Portfolio Website Design"],
            certs: ["Adobe Certified Professional"],
            questions: ["What is User Persona?", "Explain Design Thinking", "What makes good UX?"],
            companies: "Google, Adobe, Zepto, Swiggy, Design Agencies" 
        };
    }
    if(interest == "Business"){
        data = {
            career_short: "BA", career: "Business Analyst", salary: "₹6 LPA - ₹18 LPA", 
            about: "Data aur market dekh kar company ko growth me help karta hai. Tech + Business dono ka mix hai.",
            skills: ["Excel","SQL","Analytics","Communication","Leadership"], 
            roadmap: ["Month 1: Excel + SQL + PowerBI","Month 2: Business Case Studies","Month 3: Internship + LinkedIn Networking"], 
            courses: ["<a href='#' target='_blank'>Coursera: Business Analytics</a>", "<a href='#' target='_blank'>LinkedIn Learning BA</a>"],
            projects: ["Sales Forecast Model", "Customer Churn Analysis", "Market Research Report"],
            certs: ["CBAP - IIBA Certification", "Google Data Analytics"],
            questions: ["What are KPIs?", "Explain SWOT Analysis", "How to do Requirement Gathering?"],
            companies: "McKinsey, Deloitte, KPMG, Amazon, Banks, Consultancies" 
        };
    }
    
    document.getElementById("n").innerText = name;
    document.getElementById("a").innerText = age;
    document.getElementById("b").innerText = branch;
    document.getElementById("c").innerText = cgpa;
    document.getElementById("i").innerText = interest;
    document.getElementById("sub").innerText = sub;
    document.getElementById("career").innerText = data.career;
    document.getElementById("career_short").innerText = data.career_short;
    document.getElementById("salary").innerText = data.salary;
    document.getElementById("about").innerText = data.about;
    document.getElementById("skills").innerHTML = data.skills.map(s => "<span class='badge'>"+s+"</span>").join("");
    document.getElementById("roadmap").innerHTML = data.roadmap.map(s => "<li>"+s+"</li>").join("");
    document.getElementById("courses").innerHTML = data.courses.map(s => "<p>"+s+"</p>").join("");
    document.getElementById("projects").innerHTML = data.projects.map(s => "<li>"+s+"</li>").join("");
    document.getElementById("certs").innerHTML = data.certs.map(s => "<li>"+s+"</li>").join("");
    document.getElementById("questions").innerHTML = data.questions.map(s => "<li>"+s+"</li>").join("");
    document.getElementById("companies").innerText = data.companies;
    
    document.getElementById("form").style.display = "none";
    document.getElementById("report").style.display = "block";
}
</script>
</body>
</html>
"""

with open("career_app.html", "w", encoding="utf-8") as f:
    f.write(html)

webbrowser.open("career_app.html")
print("Browser me form khul gaya")