from flask import Flask, render_template_string

app = Flask(__name__)

# SVG content embedded into the HTML template
SVG_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>J'ACCUSE: Terraform Deployment Visualizer</title>
    <style>
        body {
            margin: 0;
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        svg {
            max-width: 90%;
            max-height: 90%;
        }
    </style>
</head>
<body>
    <!-- Insert the SVG content -->
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
        <!-- Window styling with dramatic French colors -->
        <defs>
            <linearGradient id="windowGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:#002395;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#ED2939;stop-opacity:1" />
            </linearGradient>
            <filter id="dropShadow">
                <feDropShadow dx="2" dy="2" stdDeviation="2" flood-opacity="0.3"/>
            </filter>
        </defs>

        <!-- Window frame -->
        <rect width="800" height="600" fill="#f0f0f0" rx="10"/>
        <rect width="800" height="40" fill="url(#windowGradient)" rx="10"/>
        <circle cx="20" cy="20" r="6" fill="#ff5f57"/>
        <circle cx="40" cy="20" r="6" fill="#ffbd2e"/>
        <circle cx="60" cy="20" r="6" fill="#28c940"/>
        <text x="400" y="25" text-anchor="middle" fill="white" font-family="Arial" font-size="14">J'ACCUSE: Terraform Deployment Visualizer</text>

        <!-- Main content area -->
        <g transform="translate(20,60)">
            <!-- Source Terraform Code -->
            <rect width="760" height="60" fill="white" rx="5" filter="url(#dropShadow)"/>
            <text x="10" y="30" font-family="monospace" font-size="14">resource "aws_instance" "scandalous_server" { instance_type = "t2.micro" }</text>
            <rect id="highlight" x="0" y="0" width="50" height="20" fill="#ED2939" opacity="0.3">
                <animate attributeName="x" 
                         values="10;60;110;160;210;260;310;360;410;460"
                         dur="10s" 
                         repeatCount="indefinite"/>
            </rect>

            <!-- Deployment Status -->
            <g transform="translate(0,80)">
                <rect width="760" height="300" fill="white" rx="5" filter="url(#dropShadow)"/>
                <text id="deployment" x="10" y="30" font-family="monospace" font-size="14" fill="#333">
                    <tspan>Initializing...</tspan>
                    <animate attributeName="textContent"
                             values="Initializing...;Downloading providers...;Planning deployment...;J'ACCUSE! Deploying resources!;Applying changes...;Deployment complete!"
                             dur="10s"
                             repeatCount="indefinite"/>
                </text>
                
                <!-- Blinking cursor -->
                <rect x="10" y="20" width="2" height="14" fill="#333">
                    <animate attributeName="opacity"
                             values="1;0;1"
                             dur="0.8s"
                             repeatCount="indefinite"/>
                </rect>
            </g>

            <!-- Resource Deployment Visualization -->
            <g transform="translate(0,400)">
                <rect width="760" height="120" fill="white" rx="5" filter="url(#dropShadow)"/>
                
                <!-- Deployment Progress Blocks -->
                <g transform="translate(10,10)">
                    <rect width="30" height="30" fill="#002395">
                        <animate attributeName="fill-opacity"
                                 values="1;0.7;1"
                                 dur="2s"
                                 repeatCount="indefinite"/>
                    </rect>
                    <!-- Additional resource deployment blocks -->
                    <rect x="40" width="30" height="30" fill="#ED2939"/>
                    <rect x="80" width="30" height="30" fill="#002395"/>
                    <rect x="120" width="30" height="30" fill="#ED2939"/>
                </g>

                <!-- Dramatic Deployment Sparkle -->
                <g id="sparkle" transform="translate(25,25)">
                    <path d="M0,0 L5,5 M0,5 L5,0" stroke="white" stroke-width="2">
                        <animate attributeName="opacity"
                                 values="0;1;0"
                                 dur="0.5s"
                                 repeatCount="indefinite"/>
                        <animateMotion
                                 path="M0,0 L100,0 L200,0 L300,0"
                                 dur="10s"
                                 repeatCount="indefinite"/>
                    </path>
                </g>
            </g>
        </g>

        <!-- Dramatic Loading Spinner -->
        <g transform="translate(750,30)">
            <circle r="10" fill="none" stroke="#002395" stroke-width="2">
                <animate attributeName="stroke-dasharray"
                         values="0,20;20,20"
                         dur="1s"
                         repeatCount="indefinite"/>
                <animateTransform attributeName="transform"
                                 type="rotate"
                                 from="0"
                                 to="360"
                                 dur="1s"
                                 repeatCount="indefinite"/>
            </circle>
        </g>
    </svg>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(SVG_CONTENT)

if __name__ == "__main__":
    app.run(debug=True)
