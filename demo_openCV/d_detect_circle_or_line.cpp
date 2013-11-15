#include <opencv/cv.h>
#include <opencv/highgui.h>
#include <math.h>
#include <iostream>
#include <fstream>
using namespace std;

#pragma comment(lib, "opencv_core220.lib")
#pragma comment(lib, "opencv_highgui220.lib")
#pragma comment(lib, "opencv_imgproc220.lib")

struct Point
{
    double fX;
    double fY;
};

Point pts[4];
double fR;

int main()
{
    //打开输出文件  
    ofstream outf("out.txt");    
    //获取cout默认输出  
    streambuf *default_buf=cout.rdbuf();   
    //重定向cout输出到文件  
    cout.rdbuf( outf.rdbuf() );  

    char* szZero = "/home/hphp/Pictures/detect_rectangle.jpg";
    char* szOne = "/home/hphp/Pictures/detect_rectangle.jpg";
    char* szRecog = "/home/hphp/Pictures/detect_rectangle.jpg";
    IplImage* imgZero = cvLoadImage(szZero, 1);
    if (!imgZero) return -1;
    IplImage* imgOne = cvLoadImage(szOne, 1);
    if (!imgOne) return -1;
    IplImage* imgRecog = cvLoadImage(szRecog, 1);
    if (!imgRecog) return -1;

    IplImage *imgEdge = NULL;
    imgEdge = cvCreateImage(cvGetSize(imgRecog),IPL_DEPTH_8U,1);
    IplImage *imgCanny = cvCreateImage(cvGetSize(imgRecog),IPL_DEPTH_8U,1);

    CvMemStorage *storage = cvCreateMemStorage(0);//内存采用默认大小

    cvCvtColor(imgZero, imgEdge,CV_BGR2GRAY);
    cvCanny(imgEdge, imgCanny, 50, 100);
    //hough变化检测刻度0直线
    cvClearMemStorage(storage);
    CvPoint* line;
    CvSeq* lines;
    lines = cvHoughLines2(imgCanny, storage, CV_HOUGH_PROBABILISTIC, 1, CV_PI/180, 50, 50, 10 );
    line = (CvPoint*)cvGetSeqElem(lines, 0);
    cvLine(imgZero, line[0], line[1], CV_RGB(255,0,0), 3, CV_AA, 0 );
    cout<<"端点1:"<< line[0].x << "," << line[0].y<<endl;
    cout<<"端点2:"<< line[1].y << "," << line[1].y<<endl;
    pts[1].fX = line[0].x;
    pts[1].fY = line[0].y;

    cvCvtColor(imgOne, imgEdge,CV_BGR2GRAY);
    cvCanny(imgEdge, imgCanny, 50, 100);
    //hough变化检测刻度1直线
    cvClearMemStorage(storage);
    lines = cvHoughLines2(imgCanny, storage, CV_HOUGH_PROBABILISTIC, 1, CV_PI/180, 50, 50, 10 );
    line = (CvPoint*)cvGetSeqElem(lines, 0);
    cvLine(imgOne, line[0], line[1], CV_RGB(255,0,0), 3, CV_AA, 0 );
    cout<<"端点1:"<< line[0].x << "," << line[0].y<<endl;
    cout<<"端点2:"<< line[1].y << "," << line[1].y<<endl;
    pts[2].fX = line[0].x;
    pts[2].fY = line[0].y;

    cvCvtColor(imgRecog, imgEdge,CV_BGR2GRAY);
    cvCanny(imgEdge, imgCanny, 50, 100);
    //hough变化圆检测
    cvClearMemStorage(storage);
    CvSeq * cir=NULL;
    cir = cvHoughCircles(imgCanny, storage, CV_HOUGH_GRADIENT, 1, imgRecog->width/10 ,80,40, 50);
    float * p=(float *)cvGetSeqElem(cir, 0);
    CvPoint pt = cvPoint(cvRound(p[0]),cvRound(p[1]));
    cvCircle(imgRecog,pt,cvRound(p[2]),CV_RGB(0,255,0));
    cvCircle(imgRecog, pt, 5, CV_RGB(0,255,0), -1, 8, 0 );//绘制圆心
    cout<<"圆心："<<pt.x<<","<<pt.y<<endl;
    cout<<"半径："<<p[2]<<endl;
    pts[0].fX = pt.x;
    pts[0].fY = pt.y;
    fR = p[2];

    //hough变化检测指针直线
    lines = cvHoughLines2(imgCanny, storage, CV_HOUGH_PROBABILISTIC, 1, CV_PI/180, 50, 50, 10 );
    line = (CvPoint*)cvGetSeqElem(lines, 0);
    cvLine(imgRecog, line[0], line[1], CV_RGB(255,0,0), 3, CV_AA, 0 );
    cout<<"端点1:"<< line[0].x << "," << line[0].y<<endl;
    cout<<"端点2:"<< line[1].y << "," << line[1].y<<endl;
    pts[3].fX = line[0].x;
    pts[3].fY = line[0].y;

    static const double PI = atan(1.0) * 4;
    double fKZero = (pts[1].fY - pts[0].fY) / (pts[1].fX - pts[0].fX);
    double fThetaZero = 180.0 / PI * atan(fKZero);
    if (pts[1].fX  + 10 < pts[0].fX)//左半部分
    {
        fThetaZero += 180.0;
    }
    fThetaZero += 360.0;
    if (fThetaZero > 360.0)
    {
        fThetaZero -= 360.0;
    }

    double fKOne = (pts[2].fY - pts[0].fY) / (pts[2].fX - pts[0].fX);
    double fThetaOne = 180.0 / PI * atan(fKOne);
    if (pts[2].fX  + 10 < pts[0].fX)//左半部分
    {
        fThetaOne += 180.0;
    }
    fThetaOne += 360.0;
    if (fThetaOne > 360.0)
    {
        fThetaOne -= 360.0;
    }

    double fKRecog = (pts[3].fY - pts[0].fY) / (pts[3].fX - pts[0].fX);
    double fThetaRecog = 180.0 / PI * atan(fKRecog);
    if (pts[3].fX  + 10 < pts[0].fX)//左半部分
    {
        fThetaRecog += 180.0;
    }
    fThetaRecog += 360.0;
    if (fThetaRecog > 360.0)
    {
        fThetaRecog -= 360.0;
    }

    char szAns[100];
    sprintf(szAns, "0刻度的角度为:%f,1刻度的角度为:%f,识别刻度的角度为:%f,识别结果为:%.2f",
            fThetaZero, fThetaOne, fThetaRecog, (fThetaRecog - fThetaZero) / (fThetaOne - fThetaZero));
    cout << szAns << endl;

    cvNamedWindow("检测", CV_WINDOW_AUTOSIZE);
    cvShowImage("检测", imgRecog);
    cvNamedWindow("刻度0", CV_WINDOW_AUTOSIZE);
    cvShowImage("刻度0", imgZero);
    cvNamedWindow("刻度1", CV_WINDOW_AUTOSIZE);
    cvShowImage("刻度1", imgOne);
    cvWaitKey(0);

    cvDestroyWindow("检测");
    cvDestroyWindow("刻度0");
    cvDestroyWindow("刻度1");
    cvReleaseImage(&imgRecog);
    cvReleaseImage(&imgZero);
    cvReleaseImage(&imgOne);
    cvReleaseImage(&imgEdge);
    cvReleaseImage(&imgCanny);
    cvReleaseMemStorage(&storage);
}

